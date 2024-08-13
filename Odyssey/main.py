from odyssey import Odyssey
from odyssey.utils import config
from odyssey.utils.logger import get_logger
from odyssey.agents.llama import ModelType

import traceback
logger = get_logger('main')
mc_port = config.get('MC_SERVER_PORT')
mc_host = config.get('MC_SERVER_HOST')
node_port = config.get('NODE_SERVER_PORT')
embedding_dir = config.get('SENTENT_EMBEDDING_DIR')
env_wait_ticks = 100
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
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='subgoal',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    # 5 classic MC tasks
    test_sub_goals = ["craft crafting table", "craft wooden pickaxe", "craft stone pickaxe", "craft iron pickaxe", "mine diamond"]
    while True:
        try:
            odyssey_l3_8b.inference_sub_goal(task="subgoal_llama3_8b_v3", sub_goals=test_sub_goals)
            odyssey_l3_70b.inference_sub_goal(task="subgoal_llama3_70b_v1", sub_goals=test_sub_goals)
        except Exception as e:
            logger.critical(e)
            traceback.print_exc()
def test_combat():
    odyssey_l3_8b_v3 = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B,
        comment_agent_model_name = ModelType.LLAMA3_8B,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B,
        planner_agent_model_name = ModelType.LLAMA3_8B,
        action_agent_model_name = ModelType.LLAMA3_8B,
    )
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
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    
    multi_rounds_tasks = ["1 zombie", "1 skeleton", "1 spider"]
    l8_v3_combat_benchmark = [
                        # Single-mob tasks
                        "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    l8_combat_benchmark = [
                        # Single-mob tasks
                         "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    l70_v1_combat_benchmark = [
                        # Single-mob tasks
                         "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    MAX_RETRY  = 3
    retry = MAX_RETRY
    while True:
        # for task in combat_benchmark:
        retry = MAX_RETRY
        i = 0
        while i < len(l8_combat_benchmark):
            try:
                odyssey_l3_8b.inference(task=l8_combat_benchmark[i], reset_env=False, feedback_rounds=1)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(l8_combat_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(multi_rounds_tasks):
            try:
                odyssey_l3_8b.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(multi_rounds_tasks[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(l70_v1_combat_benchmark):
            try:
                odyssey_l3_70b.inference(task=l70_v1_combat_benchmark[i], reset_env=False, feedback_rounds=1)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(l70_v1_combat_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(multi_rounds_tasks):
            try:
                odyssey_l3_70b.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(multi_rounds_tasks[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(l8_v3_combat_benchmark):
            try:
                odyssey_l3_8b_v3.inference(task=l8_v3_combat_benchmark[i], reset_env=False, feedback_rounds=1)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(l8_v3_combat_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(multi_rounds_tasks):
            try:
                odyssey_l3_8b_v3.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(multi_rounds_tasks[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY

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
        planner_agent_qa_model_name = ModelType.LLAMA3_8B,
        planner_agent_model_name = ModelType.LLAMA3_8B,
        action_agent_model_name = ModelType.LLAMA3_8B,
        username='bot'
    )
    odyssey_l3_8b_v3 = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
        username='bot'
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
        username='bot'
    )
    odyssey_l3_8b_v3.learn()
    odyssey_l3_8b.learn()
    odyssey_l3_70b.learn()

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
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='farming',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    farming_benchmark = [
                    "collect 1 seed (wheat or melon or pumpkin)",
                    "hoe a farmland",
                    "collect 1 wool by shearing 1 sheep",
                    "collect 1 bucket of milk",
                    "cook 1 meat (beef or mutton or pork or chicken)",
                    "obtain 1 leather",
                    "make 1 sugar",
                    "collect 1 bucket of water"
                    ]
    while True:
        # for task in farming_benchmark:
        i = 0
        while i < len(farming_benchmark):
            try:
                odyssey_l3_70b.learn(goals=farming_benchmark[i], reset_env=False)
                i += 1
            except Exception as e:
                logger.critical(farming_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc() 
        i = 0
        while i < len(farming_benchmark):
            try:
                odyssey_l3_8b.learn(goals=farming_benchmark[i], reset_env=False)
                i += 1
            except Exception as e:
                logger.critical(farming_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()

def test_skill(skill_name):
    odyssey_skill = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        resume=False,
        server_port=node_port,
    )
    odyssey_skill.run_raw_skill(f"./skill_library/skill/compositional/{skill_name}", reset=True)
    while True:
        odyssey_skill.run_raw_skill(f"./skill_library/skill/compositional/{skill_name}", reset=False)

if __name__ == '__main__':
    explore()