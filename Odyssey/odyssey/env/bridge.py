import os.path
import time
import warnings
from typing import SupportsFloat, Any, Tuple, Dict
from odyssey.utils.run_utils import retry

import requests
import json

import gymnasium as gym
from gymnasium.core import ObsType

import odyssey.utils as U

from .minecraft_launcher import MinecraftInstance
from .process_monitor import SubprocessMonitor
from odyssey.utils.logger import get_logger, Timer

class VoyagerEnv(gym.Env):
    def __init__(
        self,
        mc_host='localhost',
        mc_port=None,
        azure_login=None,
        server_host="http://127.0.0.1",
        server_port=3000,
        request_timeout=600000,
        log_path="./logs",
    ):
        if not mc_port and not azure_login:
            raise ValueError("Either mc_port or azure_login must be specified")
        if mc_port and azure_login:
            warnings.warn(
                "Both mc_port and mc_login are specified, mc_port will be ignored"
            )
        self.logger = get_logger('VoyagerEnv')
        self.mc_host = mc_host
        self.mc_port = mc_port
        self.azure_login = azure_login
        self.server = f"{server_host}:{server_port}"
        self.server_port = server_port
        self.request_timeout = request_timeout
        self.log_path = log_path
        self.mineflayer = self.get_mineflayer_process(server_port)
        if azure_login:
            self.mc_instance = self.get_mc_instance()
        else:
            self.mc_instance = None
        self.has_reset = False
        self.reset_options = None
        self.connected = False
        self.server_paused = False

    def get_mineflayer_process(self, server_port):
        U.f_mkdir(self.log_path, "mineflayer")
        file_path = os.path.abspath(os.path.dirname(__file__))
        return SubprocessMonitor(
            commands=[
                "node",
                U.f_join(file_path, "mineflayer/index.js"),
                str(server_port),
            ],
            name="mineflayer",
            ready_match=r"Server started on port (\d+)",
            log_path=U.f_join(self.log_path, "mineflayer"),
        )

    def get_mc_instance(self):
        self.logger.info('create minecraft server')
        U.f_mkdir(self.log_path, "minecraft")
        return MinecraftInstance(
            **self.azure_login,
            mineflayer=self.mineflayer,
            log_path=U.f_join(self.log_path, "minecraft"),
        )

    def check_process(self):
        if self.mc_instance and not self.mc_instance.is_running:
            # if self.mc_instance:
            #     self.mc_instance.check_process()
            #     if not self.mc_instance.is_running:
            self.logger.info('Start Minecraft server')
            self.mc_instance.run()
            self.mc_port = self.mc_instance.port
            self.reset_options["port"] = self.mc_instance.port
            self.logger.info(f"Server started on port {self.reset_options['port']}")

        if not self.mineflayer.is_running:
            retry = 3
            while retry > 0:
                self.logger.info('Start Mineflayer process')
                with Timer('check process run mineflayer'):
                    self.mineflayer.run()
                if not self.mineflayer.is_running:
                    if retry == 0:
                        raise RuntimeError("Mineflayer process failed to start")
                    else:
                        self.logger.warning('Try to restart mineflayer again, after sleep 1 second')
                        time.sleep(1)
                    retry -= 1
                else:
                    self.logger.info(f'mineflayer ready line: {self.mineflayer.ready_line}')
                    if self.mineflayer.ready_line is None:
                        self.logger.critical('mineflayer read line is None.')
                    break
            
            retry = 3
            while retry > 0:
                try:
                    res = requests.post(
                        f"{self.server}/start",
                        json=self.reset_options,
                        timeout=self.request_timeout,
                    )
                    if res.status_code == 200:
                        # self.logger.debug(f'start response:{res.json()}')
                        return res.json()
                    else:
                        if retry == 0:
                            self.mineflayer.stop()
                            raise RuntimeError("Reset Minecraft server failed!")
                        else:
                            self.logger.warning(f'Reset Minecraft server {res.status_code}')
                            time.sleep(3)
                        retry -= 1
                except requests.exceptions.Timeout:
                    if retry == 0:
                        self.mineflayer.stop()
                        raise RuntimeError("Reset Minecraft server timeout!")
                    else:
                        self.logger.warning(f"Reset Minecraft server timeout, retrying")
                        time.sleep(1)
                    retry -= 1
        else:
            self.logger.info('Mineflayer process is running')
            return None


    def step(
        self,
        code: str,
        programs: str = "",
        retry: int =3
    ) -> Tuple[ObsType, SupportsFloat, bool, bool, Dict[str, Any]]:
        if not self.has_reset:
            raise RuntimeError("Environment has not been reset yet")
        self.check_process()
        self.unpause()
        data = {
            "code": code,
            "programs": programs,
        }
        while retry > 0:
            try:
                with Timer('post step'):
                    res = requests.post(
                        f"{self.server}/step", json=data, timeout=self.request_timeout
                    )
                    if res.status_code == 200:
                        self.logger.debug(f'response:{res.json()}')
                        break
                    else:
                        retry -= 1
                        self.logger.warning(f"Step Minecraft server failed, retrying")
                        if retry == 0:
                            raise RuntimeError("Step Minecraft server failed!")
            except requests.exceptions.Timeout:
                retry -= 1
                self.logger.warning(f"Step Minecraft server timeout, retrying")
                if retry == 0:
                    raise RuntimeError("Step Minecraft server timeout!")
                res = requests.post(
                    f"{self.server}/start",
                    json=self.reset_options,
                    timeout=self.request_timeout,
                )

        
        # if res.status_code != 200:
        #     raise RuntimeError("Failed to step Minecraft server")
        returned_data = res.json()
        self.pause()
        return json.loads(returned_data)

    def render(self):
        raise NotImplementedError("render is not implemented")

    def reset(
        self,
        *,
        seed=None,
        options=None,
    ) -> Tuple[ObsType, Dict[str, Any]]:
        self.logger.info('reset node server')
        if options is None:
            options = {}

        if options.get("inventory", {}) and options.get("mode", "hard") != "hard":
            raise RuntimeError("inventory can only be set when options is hard")

        self.reset_options = {
            "host": self.mc_host,
            "port": self.mc_port,
            "reset": options.get("mode", "hard"),
            "inventory": options.get("inventory", {}),
            "equipment": options.get("equipment", []),
            "spread": options.get("spread", False),
            "waitTicks": options.get("wait_ticks", 5),
            "position": options.get("position", None),
            "username": options.get('username', 'bot')
        }
        with Timer('reset unpause mc server'):
            self.unpause()
        with Timer('reset stop mc_server'):
            self.mineflayer.stop()
        time.sleep(1)  # wait for mineflayer to exit
        with Timer('reset check_process'):
            returned_data = self.check_process()
        self.has_reset = True
        self.connected = True
        # All the reset in step will be soft
        self.reset_options["reset"] = "soft"
        self.pause()

        if returned_data is None:
            self.logger.warning('reset return None')
            return None        
        return json.loads(returned_data)

    def close(self):
        self.unpause()
        if self.connected:
            res = requests.post(f"{self.server}/stop")
            if res.status_code == 200:
                self.connected = False
        if self.mc_instance:
            self.mc_instance.stop()
        self.mineflayer.stop()
        return not self.connected

    @retry(retry_count=3)
    def pause(self):
        if self.mineflayer.is_running and not self.server_paused:
            res = requests.post(f"{self.server}/pause")
            if res.status_code == 200:
                self.server_paused = True
            else:
                self.logger.warning(f"Failed to pause Minecraft server {res.status_code}")
                raise RuntimeError("Failed to pause Minecraft server")
        return self.server_paused

    @retry(retry_count=3)
    def unpause(self):
        if self.mineflayer.is_running and self.server_paused:
            res = requests.post(f"{self.server}/pause")
            if res.status_code == 200:
                self.server_paused = False
            else:
                self.logger.warning(f"Failed to unpause Minecraft server {res.status_code}")
                raise RuntimeError("Failed to unpause Minecraft server")
                    
        return self.server_paused
