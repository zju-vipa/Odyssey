## Overview

Official codebase for the paper "[Parallelized Planning-Acting for Efficient LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.03505)".

## Demo

All demonstration videos were captured using the spectator mode within Minecraft. To comply with GitHub's file size restrictions, some videos have been accelerated.

Agents defeating the Ender Dragon:

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Multi-Agent/demo/ender_dragon.png)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Multi-Agent/demo/ender_dragon.mp4)

Agents defeating the Wither:

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Multi-Agent/demo/wither.png)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Multi-Agent/demo/wither.mp4)

# Installation and Configuration Guide

## Prerequisites
Follow the instructions in the root directory's `README.md` file to complete the [Odyssey installation](../README.md).

## Directory Description

- **odyssey**
    
    Code of the multi-agent framework.

- **MCskill**

    Code of the Minecraft comprehensive skill library.

- **MCsave**

    A pre-configured Minecraft save file for quick testing.

## Configuration Setup
Modify the `config.json` file using the following template:

```json
{
    // Provide api key that correspond to the type of model
    "openai_key": "sk-xxx",
    "dashscope_key": "sk-xxx",
    "deepseek_key": "sk-xxx",
    // If no API is provided, locally deployed LLaMa is also supported
    "server_host": "ip", // Your LLMs server ip
    "server_port": "port", // Your LLMs server port
    "NODE_SERVER_PORT": 3000, // Multiple consecutive ports from this will be occupied by multiple processes
    "MC_SERVER_HOST": "localhost", // Your Minecraft server ip
    "MC_SERVER_PORT": 25565 // Your Minecraft server port
}
```

Various models via APIs from GPT, DeepSeek, Alibaba Cloud (dashscope key) and locally deployed LLaMa are supported. For local testing, enable LAN mode within Minecraft and set the `MC_SERVER_PORT` to the port displayed by the game.

## Running

Run `main.py` while specifying the task scenario and the number of agents manually.

### Benchmark Tasks

#### Resource Collection Task

This task involves collecting specified resources. In addition to the predefined tasks，you can also define any combination of items you wish to collect in any custome Minecraft worlds instead of the provided `MCsave`'s superflat world, format them as a dictionary, and add them to a list (manually modify `RESOURCE_REQUIREMENTS` in `main.py`) for testing purposes.

```bash
python main.py resource <list_index> <num_agents>
```

#### Boss Combat Task
This task requires one of three predefined `combat_scene`: Ocean, Nether, or End. Ensure you are using the `MCsave` world for this test; otherwise, the scenarios will not be initialized correctly.

```bash
python main.py combat <combat_scene> <num_agents>
```
#### Adversarial PVP Task 

For this task, it is also strongly recommended to use the `MCsave` world. Alternatively, you may need to manually adjust the setup section of the code in `setupAPIs.js` to ensure that agent spawn points are close to each other.

```bash
python main.py pvp <num_agents>
```

If you want to change other parameters (e.g., model types, initial inventory, player names and team names), you will need to manually call the function with the appropriate parameters for testing.
