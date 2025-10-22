
<div align="center">
<img src="./Odyssey/images/logo.jpg" width="38%">
</div>
<h1 align="center">Empowering Minecraft Agents with Open-World Skills</h1>

<div align="center">
	<a href="https://arxiv.org/abs/2407.15325"><img src="https://img.shields.io/badge/arXiv-2407.15325-b31b1b.svg"/></a>
	<a href="https://github.com/zju-vipa/Odyssey/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/badge/Dataset-Released-orange"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/badge/Project-Odyssey-yellow"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://visitor-badge.laobi.icu/badge?page_id=zju-vipa.Odyssey"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/github/stars/zju-vipa/Odyssey"/></a>
</div>

Official codebase for the paper "[Odyssey: Empowering Minecraft Agents with Open-World Skills](https://arxiv.org/abs/2407.15325)". This codebase is based on the [Voyager](https://github.com/MineDojo/Voyager) framework.

<div align="center">
<img src="./Odyssey/images/framework-1.png" width="100%">
</div>

## Overview 

**Abstract:** Recent studies have delved into constructing generalist agents for open-world environments like Minecraft. Despite the encouraging results, existing efforts mainly focus on solving basic programmatic tasks, e.g., material collection and tool-crafting following the Minecraft tech-tree, treating the ObtainDiamond task as the ultimate goal. This limitation stems from the narrowly defined set of actions available to agents, requiring them to learn effective long-horizon strategies from scratch. Consequently, discovering diverse gameplay opportunities in the open world becomes challenging. In this work, we introduce Odyssey, a new framework that empowers Large Language Model (LLM)-based agents with open-world skills to explore the vast Minecraft world. Odyssey comprises three key parts: 

- **(1) An interactive agent with an open-world skill library that consists of 40 primitive skills and 183 compositional skills.**
- **(2) A fine-tuned LLaMA-3 model trained on a large question-answering dataset with 390k+ instruction entries derived from the Minecraft Wiki.**
- **(3) A new agent capability benchmark includes the long-term planning task, the dynamic-immediate planning task, and the autonomous exploration task.**

Extensive experiments demonstrate that the proposed Odyssey framework can effectively evaluate different capabilities of LLM-based agents. All datasets, model weights, and code are publicly available to motivate future research on more advanced autonomous agent solutions.


## News

- **`[Apr 29, 2025]`** 🔥 We are very happy that **ODYSSEY** has been accepted by IJCAI 2025.
- **`[Mar 5, 2025]`** 🔥 We have uploaded our new paper titled ["Parallelized Planning-Acting for Efficient LLM-based Multi-Agent Systems"](https://arxiv.org/abs/2503.03505) to arXiv. 
- **`[Feb 23, 2025]`** 🔥 We have open-sourced the [Multi-Agent Framework](https://github.com/zju-vipa/Odyssey/tree/master/Multi-Agent) to align with our latest paper. 
- **`[Oct 1, 2024]`** 🔥 We have additionally compared more baselines (with different open-sourced LLMs and agents) and designed more test scenarios (for the long-term planning task and the dynamic-immediate planning task) in the updated version of the [paper](https://arxiv.org/abs/2407.15325).
- **`[Sep 1, 2024]`** 🔥 We have additionally open-sourced the [Web Crawler Program](https://github.com/zju-vipa/Odyssey/tree/master/MC-Crawler), which was used to collect data from Minecraft Wikis. Researchers can modify this program to crawl data relevant to their needs.
- **`[Aug 14, 2024]`** 🔥 We have additionally open-sourced the [Comprehensive Skill Library](https://github.com/zju-vipa/Odyssey/tree/master/MC-Comprehensive-Skill-Library), aiming to provide an automated tool to collect all collectible and craftable items in Minecraft.
- **`[Jul 23, 2024]`** 🔥 The [paper](https://arxiv.org/abs/2407.15325) for **ODYSSEY** has been uploaded to arXiv!
- **`[Jun 13, 2024]`** 🔥 The [GitHub repository](https://github.com/zju-vipa/Odyssey) for **ODYSSEY** has been open-sourced!

## Demo

All demonstration videos were captured using the spectator mode within Minecraft. To comply with GitHub's file size restrictions, some videos have been accelerated.

Mining Diamonds from Scratch:

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/mineDiamond_preview.jpg)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/mineDiamond.mp4)

Craft Sword and Combat Zombie:

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/combatDemo_preview.jpg)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/combatDemo.mp4)

Shear a Sheep and Milk a Cow:

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/farmDemo_preview.jpg)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/farmDemo.mp4)

Autonomous Exploration: (Only First Few Rounds)

[![Watch the video](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/exploreDemo_preview.jpg)](https://raw.githubusercontent.com/zju-vipa/Odyssey/master/Odyssey/images/exploreDemo.mp4)

## Contents

- [Directory Description](#Directory-Description)
- [Odyssey Installation](#Odyssey-Installation)
  - [Python Install](#Python-Install)
  - [Node.js Install](#Node.js-Install)
  - [Minecraft Server](#Minecraft-Server)
  - [Embedding Model](#Embedding-Model)
- [Config](#Config)
- [Odyssey Tasks](#Odyssey-Tasks)
  - [Subgoal](#Subgoal)
  - [Long-term Planning Task](#Long-term-Planning-Task)
  - [Dynamic-Immediate Planning Task](#Dynamic-Immediate-Planning-Task)
  - [Autonomous Exploration Task](#Autonomous-Exploration-Task)
- [Related Works](#Related-Works)



## Directory Description

1. **LLM-Backend**

   Code to deploy LLM backend.

2. **MC-Crawler**

   Crawling Minecraft game information from Minecraft Wiki and storing data in markdown format.

3. **MineMA-Model-Fine-Tuning**

     Code to fine-tune the LLaMa model and generate training and test datasets.

4. **Odyssey**

     Code for Minecraft agents based on a large language model and skill library.

## Odyssey Installation

We use Python ≥ 3.9 and Node.js ≥ 16.13.0. We have tested on Ubuntu 20.04, Windows 10, and macOS.

### Python Install

```bash
cd Odyssey
pip install -e .
pip install -r requirements.txt
```

### Node.js Install

```bash
npm install -g yarn
cd Odyssey/odyssey/env/mineflayer
yarn install
cd Odyssey/odyssey/env/mineflayer/mineflayer-collectblock
npx tsc
cd Odyssey/odyssey/env/mineflayer
yarn install
cd Odyssey/odyssey/env/mineflayer/node_modules/mineflayer-collectblock
npx tsc
```

### Minecraft Server

You can deploy a Minecraft server using docker. See [here](./Odyssey/docs/run_using_docker.md).

### Embedding Model

1. Need to install [git-lfs](https://git-lfs.com) first.

2. Download the embedding model repository

   ```bash
   git lfs install
   git clone https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2.git
   ```

3. The directory where you clone the repository is then used to set `embedding_dir`.

## Config

You need to create `config.json` according to the format of `conf/config.json.keep.this` in `conf` directory.

- `server_host`: LLaMa backend server ip.
- `server_port`: LLaMa backend server port.
- `NODE_SERVER_PORT`: Node service port.
- `SENTENT_EMBEDDING_DIR`: Path to your embedding model.
- `MC_SERVER_HOST`: Minecraft server ip.
- `MC_SERVER_PORT`: Minecraft server port.

## Get Started

After completing the above installation and configuration, you can start the agent by simply running `python main.py`. To operate the agent under different task scenarios, manually modify the function you wish to execute. Below are the task scenarios.

## Odyssey Tasks

### Subgoal

```python
def test_subgoal():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='subgoal',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        curriculum_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        curriculum_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    # 5 classic MC tasks
    test_sub_goals = ["craft crafting table", "craft wooden pickaxe", "craft stone pickaxe", "craft iron pickaxe", "mine diamond"]
    try:
        odyssey_l3_8b.inference_sub_goal(task="subgoal_llama3_8b_v3", sub_goals=test_sub_goals)
    except Exception as e:
        print(e)
```

| Model                          | For what                                                     |
| ------------------------------ | ------------------------------------------------------------ |
| action_agent_model_name        | Choose one of the k retrieved skills to execute              |
| curriculum_agent_model_name    | Propose tasks for farming and explore                        |
| curriculum_agent_qa_model_name | Schedule subtasks for combat, generate QA context, and rank the order to kill monsters |
| critic_agent_model_name        | Action critic                                                |
| comment_agent_model_name       | Give the critic about the last combat result, in order to reschedule subtasks for combat |

### Long-term Planning Task

```python
def test_combat():
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        curriculum_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        curriculum_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    
    multi_rounds_tasks = ["1 enderman", "3 zombie"]
    l70_v1_combat_benchmark = [
                        # Single-mob tasks
                         "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider"
                        ]
    for task in l70_v1_combat_benchmark:
        odyssey_l3_70b.inference(task=task, reset_env=False, feedback_rounds=1)
    for task in multi_rounds_tasks:
        odyssey_l3_70b.inference(task=task, reset_env=False, feedback_rounds=3)
```

### Dynamic-Immediate Planning Task

```python
def test_farming():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='farming',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        curriculum_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        curriculum_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )

    farming_benchmark = [
                    # Single-goal tasks
                    "collect 1 wool by shearing 1 sheep",
                    "collect 1 bucket of milk",
                    "cook 1 meat (beef or mutton or pork or chicken)",
                    # Multi-goal tasks
                    "collect and plant 1 seed (wheat or melon or pumpkin)"
                    ]
   	for goal in farming_benchmark:
	      odyssey_l3_8b.learn(goals=goal, reset_env=False)
```

### Autonomous Exploration Task

```python
def explore():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B,
        comment_agent_model_name = ModelType.LLAMA3_8B,
        curriculum_agent_qa_model_name = ModelType.LLAMA3_8B,
        curriculum_agent_model_name = ModelType.LLAMA3_8B,
        action_agent_model_name = ModelType.LLAMA3_8B,
        username='bot1_8b'
    )
    odyssey_l3_8b.learn()
```



## Related Works

| **ID** |                          **Paper**                           |                         **Authors**                          |         Venue          |
| :----: | :----------------------------------------------------------: | :----------------------------------------------------------: | :--------------------: |
|   1    | [MineRL: A Large-Scale Dataset of Minecraft Demonstrations](https://arxiv.org/abs/1907.13440) | William H. Guss, Brandon Houghton, Nicholay Topin, Phillip Wang, Cayden Codel, Manuela Veloso, Ruslan Salakhutdinov |       IJCAI 2019       |
|   2    | [Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos](https://arxiv.org/abs/2206.11795) | Bowen Baker, Ilge Akkaya, Peter Zhokhov, Joost Huizinga, Jie Tang, Adrien Ecoffet, Brandon Houghton, Raul Sampedro, Jeff Clune |       arXiv 2022       |
|   3    | [MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge](https://arxiv.org/abs/2206.08853) | Linxi Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu, Andrew Tang, De-An Huang, Yuke Zhu, Anima Anandkumar |      NeurIPS 2022      |
|   4    | [Open-World Multi-Task Control Through Goal-Aware Representation Learning and Adaptive Horizon Prediction](https://arxiv.org/abs/2301.10034) | Shaofei Cai, Zihao Wang, Xiaojian Ma, Anji Liu, Yitao Liang  |       CVPR 2023        |
|   5    | [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/abs/2302.01560) | Zihao Wang, Shaofei Cai, Guanzhou Chen, Anji Liu, Xiaojian Ma, Yitao Liang |      NeurIPS 2023      |
|   6    | [Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks](https://arxiv.org/abs/2303.16563) | Haoqi Yuan, Chi Zhang, Hongcheng Wang, Feiyang Xie, Penglin Cai, Hao Dong, Zongqing Lu | NeurIPS Workshop  2023 |
|   7    | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar |       arXiv 2023       |
|   8    | [Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory](https://arxiv.org/abs/2305.17144) | Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu, Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, Jifeng Dai |       arXiv 2023       |
|   9    | [STEVE-1: A Generative Model for Text-to-Behavior in Minecraft](https://arxiv.org/abs/2306.00937) | Shalev Lifshitz, Keiran Paster, Harris Chan, Jimmy Ba, Sheila McIlraith |      NeurIPS 2023      |
|   10   | [GROOT: Learning to Follow Instructions by Watching Gameplay Videos](https://arxiv.org/abs/2310.08235) | Shaofei Cai, Bowei Zhang, Zihao Wang, Xiaojian Ma, Anji Liu, Yitao Liang |       arXiv 2023       |
|   11   | [MCU: A Task-centric Framework for Open-ended Agent Evaluation in Minecraft](https://arxiv.org/abs/2310.08367) |       Haowei Lin, Zihao Wang, Jianzhu Ma, Yitao Liang        |       arXiv 2023       |
|   12   | [LLaMA Rider: Spurring Large Language Models to Explore the Open World](https://arxiv.org/abs/2310.08922) | Yicheng Feng, Yuxuan Wang, Jiazheng Liu, Sipeng Zheng, Zongqing Lu |       arXiv 2023       |
|   13   | [JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models](https://arxiv.org/abs/2311.05997) | Zihao Wang, Shaofei Cai, Anji Liu, Yonggang Jin, Jinbing Hou, Bowei Zhang, Haowei Lin, Zhaofeng He, Zilong Zheng, Yaodong Yang, Xiaojian Ma, Yitao Liang |       arXiv 2023       |
|   14   | [See and Think: Embodied Agent in Virtual Environment](https://arxiv.org/abs/2311.15209) | Zhonghan Zhao, Wenhao Chai, Xuan Wang, Li Boyi, Shengyu Hao, Shidong Cao, Tian Ye, Jenq-Neng Hwang, Gaoang Wang |       arXiv 2023       |
|   15   | [Creative Agents: Empowering Agents with Imagination for Creative Tasks](https://arxiv.org/abs/2312.02519) |  Chi Zhang, Penglin Cai, Yuhui Fu, Haoqi Yuan, Zongqing Lu   |       arXiv 2023       |
|   16   | [MP5: A Multi-modal Open-ended Embodied System in Minecraft via Active Perception](https://arxiv.org/abs/2312.07472) | Yiran Qin, Enshen Zhou, Qichang Liu, Zhenfei Yin, Lu Sheng, Ruimao Zhang, Yu Qiao, Jing Shao |       arXiv 2024       |
|   17   | [Auto MC-Reward: Automated Dense Reward Design with Large Language Models for Minecraft](https://arxiv.org/abs/2312.09238) | Hao Li, Xue Yang, Zhaokai Wang, Xizhou Zhu, Jie Zhou, Yu Qiao, Xiaogang Wang, Hongsheng Li, Lewei Lu, Jifeng Dai |       arXiv 2024       |
|   18   | [MrSteve: Instruction-Following Agents in Minecraft with What-Where-When Memory](https://arxiv.org/abs/2411.06736) | Junyeong Park, Junmo Cho, Sungjin Ahn |       arXiv 2024       |
|   19   | [Project Sid: Many-agent simulations toward AI civilization](https://arxiv.org/abs/2411.00114) | Altera.AL, Andrew Ahn, Nic Becker, Stephanie Carroll, Nico Christie, Manuel Cortes, Arda Demirci, Melissa Du, Frankie Li, Shuying Luo, Peter Y Wang, Mathew Willows, Feitong Yang, Guangyu Robert Yang |       arXiv 2024       |
|   20   | [ADAM: An Embodied Causal Agent in Open-World Environments](https://arxiv.org/abs/2410.22194) | Shu Yu, Chaochao Lu |       arXiv 2024       |
|   21   | [WALL-E: World Alignment by Rule Learning Improves World Model-based LLM Agents](https://arxiv.org/abs/2410.07484) | Siyu Zhou, Tianyi Zhou, Yijun Yang, Guodong Long, Deheng Ye, Jing Jiang, Chengqi Zhang |       arXiv 2024       |
|   22   | [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://arxiv.org/abs/2408.03615) | Zaijing Li, Yuquan Xie, Rui Shao, Gongwei Chen, Dongmei Jiang, Liqiang Nie |       NeurIPS 2024       |
|   23   | [OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://arxiv.org/abs/2407.00114) | Zihao Wang, Shaofei Cai, Zhancun Mu, Haowei Lin, Ceyao Zhang, Xuejie Liu, Qing Li, Anji Liu, Xiaojian Ma, Yitao Liang |       NeurIPS 2024       |
|   24   | [VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft](https://arxiv.org/abs/2406.05720) | Yubo Dong, Xukun Zhu, Zhengzhe Pan, Linchao Zhu, Yi Yang |       ACL 2024       |
|   25   | [GROOT-2: Weakly Supervised Multi-Modal Instruction Following Agents](https://arxiv.org/abs/2412.10410) | Shaofei Cai, Bowei Zhang, Zihao Wang, Haowei Lin, Xiaojian Ma, Anji Liu, Yitao Liang |       arXiv 2024       |


## Citation

If you find this work useful for your research, please cite our paper:

```
@inproceedings{liu2025odyssey,
  title={Odyssey: Empowering Minecraft Agents with Open-World Skills},
  author={Shunyu Liu and Yaoru Li and Kongcheng Zhang and Zhenyu Cui and Wenkai Fang and Yuxuan Zheng and Tongya Zheng and Mingli Song},
  booktitle={International Joint Conference on Artificial Intelligence},
  year={2025}
}

@article{li2025parallelized,
  title={Parallelized Planning-Acting for Efficient LLM-based Multi-Agent Systems},
  author={Li, Yaoru and Liu, Shunyu and Zheng, Tongya and Song, Mingli},
  journal={arXiv preprint arXiv:2503.03505},
  year={2025}
}
```

# License

| Component        | License                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Codebase](https://github.com/zju-vipa/Odyssey)     | [MIT License](https://github.com/zju-vipa/Odyssey/blob/master/LICENSE)                                                                                                  |
| [Minecraft Q&A Dataset](https://huggingface.co/datasets/Aiwensile2/Minecraft_QA-pairs_Instruction_Dataset)    | [Creative Commons Attribution Non Commercial Share Alike 3.0 Unported (CC BY-NC-SA 3.0)](https://creativecommons.org/licenses/by-nc-sa/3.0/) |


## Contact

This project is developed by [VIPA Lab](https://www.vipazoo.cn/) from Zhejiang University. Please feel free to contact me via email (<liushunyu@zju.edu.cn>) if you are interested in our research :)

<div align="center">
<img src="./Odyssey/images/vipa-logo.jpg" width="30%">
</div>

