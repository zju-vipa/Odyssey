import os
import sys
import time
import random
import concurrent.futures
from typing import Dict
from multiprocessing import Process, Manager
from odyssey import Odyssey
from odyssey.utils import config
from odyssey.agents.llm import ModelType
from odyssey.utils.logger import get_logger
from odyssey.utils.experiment import distribute_initial_resource

# GLOBAL CONSTANTS
mc_port = config.get('MC_SERVER_PORT')
mc_host = config.get('MC_SERVER_HOST')
base_node_port = config.get('NODE_SERVER_PORT')
env_wait_ticks = 100
logger = get_logger("MC-Multi-Agent")
item_dict = {
    'diamond_pickaxe': 1,
    'diamond_sword': 1,
    'diamond_helmet': 1,
    'diamond_chestplate': 1,
    'diamond_leggings': 1,
    'diamond_boots': 1,
    'bow': 1,
    'arrow': 200,
    'golden_apple': 4
} # default init_inventory in combat / pvp task

def test_skill(node_port, username, func_call_str):
    '''Single-agent skill test'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        task_scenario='skill',
        viewer_port=node_port + 100
    )
    odyssey.env_reset(mode="hard")
    odyssey.run_skill_func(func_call_str=func_call_str, log_time=True)
    odyssey.close()

def autonomous_play(node_port, username, mode, model_type, model_id, team_name, team_prompt):
    '''Multi-agent auto-play'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        model_id=model_id,
        task_scenario='explore',
        team_name=team_name,
        team_prompt=team_prompt,
        model_type=model_type,
        viewer_port=node_port + 100
    )
    odyssey.env_reset(mode="hard")
    odyssey.start_agent(mode=mode)

def resource_task(node_port, username, mode, model_type, model_id, resource_requirements, team_name, team_prompt):
    '''Resource collection task'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        model_id=model_id,
        task_scenario='resource',
        team_name=team_name,
        team_prompt=team_prompt,
        model_type=model_type,
        viewer_port=node_port + 100
    )
    odyssey.env_reset(mode="hard")
    odyssey.start_agent(item_dict=resource_requirements, mode=mode)

def combat_task(node_port, username, mode, model_type, model_id, init_inventory, test_scene, team_name, team_prompt):
    '''Boss combat task'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        model_id=model_id,
        task_scenario='combat',
        team_name=team_name,
        team_prompt=team_prompt,
        model_type=model_type,
        viewer_port=node_port + 100
    )
    odyssey.env_reset(mode="hard")
    odyssey.start_agent(item_dict=init_inventory, combat_scene=test_scene, mode=mode)

def agent_pvp(node_port, username, mode, model_type, model_id, team_name, team_prompt, init_inventory, exe_mode):
    '''Adversarial PVP task'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        model_id=model_id,
        task_scenario='pvp',
        team_name=team_name,
        team_prompt=team_prompt,
        model_type=model_type,
        viewer_port=node_port + 100,
    )
    odyssey.env_reset(mode="hard")
    if exe_mode == 'parallel':
        odyssey.start_agent(item_dict=init_inventory, mode=mode)
    elif exe_mode == 'serial':
        odyssey.start_agent_serially(item_dict=init_inventory)

def system_controller(node_port, username, team_name, task_scenario, item_dict, combat_scene, username_list):
    '''MAS control'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        task_scenario=task_scenario,
        server_port=node_port,
        username=username,
        team_name=team_name
    )
    odyssey.system_controller(team_name, item_dict, combat_scene, username_list)

def human_player_listener(node_port, username, team_name, human_player_name):
    '''Human-agent interaction'''
    odyssey = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        server_port=node_port,
        username=username,
        team_name=team_name
    )
    odyssey.human_player_listener(human_player_name, team_name)

def initialize_agents(agent_count=5, base_port=3001, username_list=[], base_username="bot", base_model_id=1, 
                      para_dict={}, model_type=ModelType.LLAMA3_8B, target_func=None, max_retries=5):
    """Initialize the agents and distribute resources if necessary."""
    # Ensure username_list's length does not exceed agent_count
    if username_list and len(username_list) > agent_count:
        username_list = username_list[:agent_count]

    agents = [
        {'port': base_port + i, 
         'username': username_list[i] if username_list and len(username_list) >= agent_count else f"{base_username}{i+1}",
         'model_id': base_model_id + i}
        for i in range(agent_count)
    ]

    manager = Manager()
    item_dict_list = manager.list()  # Use a managed list to share between processes

    if target_func == combat_task:
        # Ensure para_dict is a dictionary
        if not isinstance(para_dict, dict):
            raise ValueError("para_dict must be a dictionary of item requirements.")
        
        # Continuously try to distribute resources until a valid distribution is obtained or max retries reached
        for attempt in range(max_retries):
            try:
                item_dict_list.extend(distribute_initial_resource(agent_count, para_dict, model_type=model_type))
                break
            except Exception as e:
                time.sleep(1)  # Wait a moment before retrying
        else:
            return None, None

    return agents, item_dict_list

def start_agents(agent_count=5, team_name='A', target_func=test_skill, mode='text', base_port=3001, username_list=[], 
                 human_player=None, base_username="bot", model_type=ModelType.LLAMA3_8B, base_model_id=1, exe_mode = None,
                 para_dict={}, func_str_lst=[], confrontation_prompt='', combat_test_scene='', delay=0.1, max_retries=5):
    """Start the agents and manage their processes."""
    # Initialize agents and get the necessary data
    agents, item_dict_list = initialize_agents(
        agent_count=agent_count,
        base_port=base_port,
        username_list=username_list,
        base_username=base_username,
        base_model_id=base_model_id,
        para_dict=para_dict,
        model_type=model_type,
        target_func=target_func,
        max_retries=max_retries
    )

    if agents is None or item_dict_list is None:
        logger.failed("Failed to initialize agents. Exiting.")
        return

    processes = []
    team_members = username_list[:agent_count]

    for i, agent in enumerate(agents):
        if target_func == resource_task:
            # Ensure para_dict is a dictionary
            if not isinstance(para_dict, dict):
                raise ValueError("para_dict must be a dictionary of item requirements.")
            team_prompt = f"Your team's name is '{team_name}'. Your team members are: {', '.join(team_members)}. {confrontation_prompt}"
            process = Process(target=target_func, args=(agent['port'], agent['username'], mode, model_type, agent['model_id'], para_dict, team_name, team_prompt))
        elif target_func == combat_task:
            team_prompt = f"Your team's name is '{team_name}'. Your team members are: {', '.join(team_members)}. {confrontation_prompt}"
            process = Process(target=target_func, args=(agent['port'], agent['username'], mode, model_type, agent['model_id'], item_dict_list[i], combat_test_scene, team_name, team_prompt))
        elif target_func == test_skill:
            # Check if func_str_lst has enough elements for the number of agents
            if len(func_str_lst) < agent_count:
                raise ValueError("func_str_lst must have at least the same number of elements as agent_count.")
            process = Process(target=target_func, args=(agent['port'], agent['username'], func_str_lst[i], para_dict))
        elif target_func == autonomous_play:
            team_prompt = (f"Your team's name is '{team_name}'. Your team members are: {', '.join(team_members)}. {confrontation_prompt}"
                           f"{f' And a human player {human_player} will be with you!' if human_player else ''}")
            process = Process(target=target_func, args=(agent['port'], agent['username'], mode, model_type, agent['model_id'], team_name, team_prompt))
        elif target_func == agent_pvp:
            team_prompt = confrontation_prompt
            process = Process(target=target_func, args=(agent['port'], agent['username'], mode, model_type, agent['model_id'], team_name, team_prompt, para_dict, exe_mode))

        process.start()
        processes.append(process)
        time.sleep(delay)

    if human_player:
        # Add the process of listening to the human player
        listen_human_process = Process(target=human_player_listener, args=(5000, 'listener', team_name, human_player))
        listen_human_process.start()
        processes.append(listen_human_process)

    task_scenario = 'resource' if target_func == resource_task else 'combat' if target_func == combat_task else None
    if task_scenario:
        # Add the process of the system controller
        system_controller_process=Process(target=system_controller, args=(4000 + random.randint(0, 999), 'SystemInfo', team_name, task_scenario, para_dict, combat_test_scene, username_list))
        system_controller_process.start()
        processes.append(system_controller_process)

    # Wait for all processes to complete
    for process in processes:
        process.join()
        
    return True

def agents_confrontation(team_agent_count=1, team_a_name='A', team_b_name='B', team_a_base_port=3001, team_b_base_port=3006, 
                         team_a_username_list=['Alex', 'Steve', 'Brine', 'Chris', 'Mike'], team_b_username_list=['Notch', 'Jeb', 'David', 'Mark', 'John'], team_a_model_type=ModelType.ALI, team_b_model_type=ModelType.ALI, 
                         team_a_model_id=1, team_b_model_id=6, team_a_item_dict=item_dict, team_b_item_dict=item_dict):
    """Simulation of two teams playing against each other in a given task scene"""
    team_a_prompt = (
        f"You belong to team {team_a_name}. "
        f"Your team members are: {', '.join(team_a_username_list)}. "
        f"Your opponent is team {team_b_name}. "
        f"Their team members are: {', '.join(team_b_username_list)}."
    )
    team_b_prompt = (
        f"You belong to team {team_b_name}. "
        f"Your team members are: {', '.join(team_b_username_list)}. "
        f"Your opponent is team {team_a_name}. "
        f"Their team members are: {', '.join(team_a_username_list)}."
    )

    process_team_a = Process(target=start_agents, kwargs={
        'agent_count': team_agent_count,
        'team_name': team_a_name,
        'target_func': agent_pvp,
        'base_port': team_a_base_port,
        'username_list': team_a_username_list,
        'base_model_id': team_a_model_id,
        'confrontation_prompt': team_a_prompt,
        'model_type': team_a_model_type,
        'para_dict': team_a_item_dict,
        'exe_mode': 'parallel'
    })
    process_team_a.start()

    process_team_b = Process(target=start_agents, kwargs={
        'agent_count': team_agent_count,
        'team_name': team_b_name,
        'target_func': agent_pvp,
        'base_port': team_b_base_port,
        'username_list': team_b_username_list,
        'base_model_id': team_b_model_id,
        'confrontation_prompt': team_b_prompt,
        'model_type': team_b_model_type,
        'para_dict': team_b_item_dict,
        'exe_mode': 'serial'
    })
    process_team_b.start()

    process_team_a.join()
    process_team_b.join()

def run_combat_experiment(scene: str, agent_count: int, timeout: int = 1000, base_node_port: int = base_node_port, item_dict: Dict = item_dict):
    """Run a combat experiment with multiple agents."""
    logger.info(f"Starting experiment with scene={scene}, agent_count={agent_count}")

    # Run the experiment with a timeout
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            start_agents,
            target_func=combat_task,
            base_port=base_node_port,
            agent_count=agent_count,
            username_list=["Steve", "Alex", "Notch", "Jeb", "Brine", "Mike", "Chris", "David", "John", "Mark", "Bob", "Eric", "Frank", "Greg", "Henry"][:agent_count],
            model_type=ModelType.ALI,
            para_dict={key: value * agent_count for key, value in item_dict.items()},
            combat_test_scene=scene
        )
        try:
            result = future.result(timeout=timeout)
            logger.info(f"Experiment result: {result}")
        except concurrent.futures.TimeoutError:
            logger.info(f"Experiment timed out after {timeout} seconds.")
            os._exit(0)  # Force exit the program immediately

def run_resource_experiment(resource_requirement: dict, agent_count: int, timeout: int = 3600, base_node_port: int = base_node_port):
    """Run a resource experiment with multiple agents."""
    logger.info(f"Starting resource experiment with resource_requirement={resource_requirement}, agent_count={agent_count}")

    # Run the experiment with a timeout
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            start_agents,
            target_func=resource_task,
            base_port=base_node_port,
            agent_count=agent_count,
            username_list=["Steve", "Alex", "Notch", "Jeb", "Brine", "Mike", "Chris", "David", "John", "Mark"][:agent_count],
            model_type=ModelType.ALI,
            para_dict=resource_requirement
        )
        try:
            result = future.result(timeout=timeout)
            logger.info(f"Experiment result: {result}")
        except concurrent.futures.TimeoutError:
            logger.info(f"Experiment timed out after {timeout} seconds.")
            os._exit(0)  # Force exit the program immediately

if __name__ == '__main__':

    exp = sys.argv[1]

    if exp == 'combat':
        if len(sys.argv) > 3:
            scene = sys.argv[2]
            agent_count = int(sys.argv[3])
            run_combat_experiment(scene, agent_count)
        else:
            logger.error("Please provide the scene name and agent_count as command-line arguments.")
            sys.exit(1)
    elif exp == 'resource':
        RESOURCE_REQUIREMENTS = [
            # {'dirt': 1}, # for debugging
            {'map': 1, 'compass': 1, 'clock': 1}, # navigation set
            {'barrel': 1, 'hopper': 1, 'chest': 1}, # storage system
            {'stone_bricks': 16, 'glass': 4, 'iron_door': 1}, # building materials
            {'diamond': 24}, # diamond armor set
            {'iron_ingot': 9}, # iron tool set
            {'repeater': 1, 'dropper': 1, 'piston': 1}, # redstone set
            {'minecart': 1, 'rail': 16, 'powered_rail' : 6}, # transportation set
            {'beef': 1, 'porkchop': 1, 'chicken': 1}, # food supplies
            # add more
        ]
        
        if len(sys.argv) > 3:
            resource_index = int(sys.argv[2])
            agent_count = int(sys.argv[3])

            if resource_index < 0 or resource_index >= len(RESOURCE_REQUIREMENTS):
                logger.error(f"Invalid resource index: {resource_index}. Valid range is 0 to {len(RESOURCE_REQUIREMENTS) - 1}.")
                sys.exit(1)

            resource_requirement = RESOURCE_REQUIREMENTS[resource_index]
            
            run_resource_experiment(resource_requirement, agent_count)
        else:
            logger.error("Please provide the resource index and agent_count as command-line arguments.")
            sys.exit(1)
    elif exp == 'pvp':
        agents_confrontation(team_agent_count=int(sys.argv[2]))
    else:
        logger.error(f"Unknown experiment type: {exp}")
        sys.exit(1)