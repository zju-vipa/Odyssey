# Odyssey: Empowering Agents with Open-World Skills

<div align="center">
	<a href="https://github.com/zju-vipa/Odyssey/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/badge/Dataset-Released-orange"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/badge/Awesome-ODYSSEY-blue"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://visitor-badge.laobi.icu/badge?page_id=zju-vipa.Odyssey"/></a>
	<a href="https://github.com/zju-vipa/Odyssey"><img src="https://img.shields.io/github/stars/zju-vipa/Odyssey"/></a>
</div>

Official codebase for paper "Odyssey: Empowering Agents with Open-World Skills". This codebase is based on the [MineDojo](https://github.com/MineDojo/MineDojo) and [Voyager](https://github.com/MineDojo/Voyager) framework.

<div align="center">
<img src="./Odyssey/images/framework.png" width="100%">
</div>


## Release
- [Jun 13, 2024] 🔥 The [GitHub repository]([https://github.com/zijianchen98/GAIA](https://github.com/zju-vipa/Odyssey)) for **ODYSSEY** has been open-sourced!


## Directory Description

1. **LLM-Backend**

   Code to deploy LLM backend.

2. **MC-Crawler**

   Crawling Minecraft game information from Minecraft Wiki, and store data in markdown format.

3. **MineMA-Model-Fine-Tuning**

     Code to fine-tune the LLaMa model and genearte training and test datasets.

4. **Odyssey**

     Code for Minecaft agents based on a large language model and skill base.

## Odyssey Installation

We use Python ≥ 3.9 and Node.js ≥ 16.13.0. We have tested on Ubuntu 20.04, Windows 10, and macOS.

### Python Install

```bash
pip install -e .
pip install -r requirements.txt
```

### Node.js Install

```bash
npm install -g yarn
cd odyssey/env/mineflayer
yarn install
cd odyssey/env/mineflayer/mineflayer-collectblock
npx tsc
cd odyssey/env/mineflayer
yarn install
cd odyssey/env/mineflayer/node_modules/mineflayer-collectblock
npx tsc
```

### Minecraft Server

You can deploy a Minecraft server using docker. See [here](installation/run_using_docker.md).

### Embedding Model

1. Need to install [git-lfs](https://git-lfs.com) first.

2. Download mebedding model repository

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

1. **MineRL: A Large-Scale Dataset of Minecraft Demonstrations.** *William H. Guss, Brandon Houghton, Nicholay Topin, Phillip Wang, Cayden Codel, Manuela Veloso, Ruslan Salakhutdinov.* IJCAI, 2019. [[paper]](https://arxiv.org/abs/1907.13440)  
2. **Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online Videos.** *Bowen Baker, Ilge Akkaya, Peter Zhokhov, Joost Huizinga, Jie Tang, Adrien Ecoffet, Brandon Houghton, Raul Sampedro, Jeff Clune.* arXiv, 2022. [[paper]](https://arxiv.org/abs/2206.11795)
3. **MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge.** *Linxi Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu, Andrew Tang, De-An Huang, Yuke Zhu, Anima Anandkumar.* NeurIPS, 2022. [[paper]](https://arxiv.org/abs/2206.08853)
4. **Open-World Multi-Task Control Through Goal-Aware Representation Learning and Adaptive Horizon Prediction.** *Shaofei Cai, Zihao Wang, Xiaojian Ma, Anji Liu, Yitao Liang.* CVPR, 2023. [[paper]](https://arxiv.org/abs/2301.10034)
5. **Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents.** *Zihao Wang, Shaofei Cai, Guanzhou Chen, Anji Liu, Xiaojian Ma, Yitao Liang.* NeurIPS, 2023. [[paper]](https://arxiv.org/abs/2302.01560)
6. **A Survey on Game Playing Agents and Large Models: Methods, Applications, and Challenges.** *Xinrun Xu, Yuxin Wang, Chaoyi Xu, Ziluo Ding, Jiechuan Jiang, Zhiming Ding, Börje F. Karlsson.* arXiv, 2024. [[paper]](https://arxiv.org/abs/2403.10249)
7. **Skill Reinforcement Learning and Planning for Open-World Long-Horizon Tasks.** *Haoqi Yuan, Chi Zhang, Hongcheng Wang, Feiyang Xie, Penglin Cai, Hao Dong, Zongqing Lu.* NeurIPS Workshop, 2023. [[paper]](https://arxiv.org/abs/2303.16563)
8. **Voyager: An Open-Ended Embodied Agent with Large Language Models.** *Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar.* arXiv, 2023. [[paper]](https://arxiv.org/abs/2305.16291)
9. **Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory.** *Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu, Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, Jifeng Dai.* arXiv, 2023. [[paper]](https://arxiv.org/abs/2305.17144)
10. **STEVE-1: A Generative Model for Text-to-Behavior in Minecraft.** *Shalev Lifshitz, Keiran Paster, Harris Chan, Jimmy Ba, Sheila McIlraith.* NeurIPS, 2023. [[paper]](https://arxiv.org/abs/2306.00937)
11. **GROOT: Learning to Follow Instructions by Watching Gameplay Videos.** *Shaofei Cai, Bowei Zhang, Zihao Wang, Xiaojian Ma, Anji Liu, Yitao Liang.* arXiv, 2023. [[paper]](https://arxiv.org/abs/2310.08235)
12. **MCU: A Task-centric Framework for Open-ended Agent Evaluation in Minecraft.** *Haowei Lin, Zihao Wang, Jianzhu Ma, Yitao Liang.* arXiv, 2023. [[paper]](https://arxiv.org/abs/2310.08367)
13. **LLaMA Rider: Spurring Large Language Models to Explore the Open World.** *Yicheng Feng, Yuxuan Wang, Jiazheng Liu, Sipeng Zheng, Zongqing Lu.* arXiv 2023. [[paper]](https://arxiv.org/abs/2310.08922)
14. **JARVIS-1: Open-World Multi-task Agents with Memory-Augmented Multimodal Language Models.** *Zihao Wang, Shaofei Cai, Anji Liu, Yonggang Jin, Jinbing Hou, Bowei Zhang, Haowei Lin, Zhaofeng He, Zilong Zheng, Yaodong Yang, Xiaojian Ma, Yitao Liang.*  arXiv, 2023. [[paper]](https://arxiv.org/abs/2311.05997)
15. **See and Think: Embodied Agent in Virtual Environment.** *Zhonghan Zhao, Wenhao Chai, Xuan Wang, Li Boyi, Shengyu Hao, Shidong Cao, Tian Ye, Jenq-Neng Hwang, Gaoang Wang.* arXiv, 2023. [[paper]](https://arxiv.org/abs/2311.15209)
16. **Creative Agents: Empowering Agents with Imagination for Creative Tasks.** *Chi Zhang, Penglin Cai, Yuhui Fu, Haoqi Yuan, Zongqing Lu.* arXiv 2023. [[paper]](https://arxiv.org/abs/2312.02519)
17. **MP5: A Multi-modal Open-ended Embodied System in Minecraft via Active Perception.** *Yiran Qin, Enshen Zhou, Qichang Liu, Zhenfei Yin, Lu Sheng, Ruimao Zhang, Yu Qiao, Jing Shao.* arXiv, 2024. [[paper]](https://arxiv.org/abs/2312.07472)
18. **Auto MC-Reward: Automated Dense Reward Design with Large Language Models for Minecraft.** *Hao Li, Xue Yang, Zhaokai Wang, Xizhou Zhu, Jie Zhou, Yu Qiao, Xiaogang Wang, Hongsheng Li, Lewei Lu, Jifeng Dai.* arXiv, 2024. [[paper]](https://arxiv.org/abs/2312.09238)


## Contact

Please feel free to contact me via email (<liushunyu@zju.edu.cn>) if you are interested in my research :)

