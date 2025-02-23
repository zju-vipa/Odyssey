import re
import time
import json
from typing import List, Dict
from langchain.schema import AIMessage, SystemMessage, HumanMessage
from odyssey.utils import config
from odyssey.agents.llm import call_with_messages
from odyssey.prompts import load_prompt
from odyssey.utils.logger import get_logger

logger = get_logger("MC-Multi-Agent")
mc_port = config.get('MC_SERVER_PORT')
mc_host = config.get('MC_SERVER_HOST')
base_node_port = config.get('NODE_SERVER_PORT')
env_wait_ticks = 100

def extract_json_list(content: str) -> List[Dict]:
    """Extracts a JSON list from a string that may contain additional text."""
    # Use regex to find the first JSON list in the content
    match = re.search(r'\[.*\]', content, re.DOTALL)
    if not match:
        raise ValueError("No JSON list found in the response content.")

    # Extract the matched JSON list
    json_str = match.group(0)

    try:
        # Parse the JSON list
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON list: {e}")
    
def distribute_initial_resource(agent_count, item_dict, model_type, max_retries=5):
    """Distributes the resources among agents using an LLM to generate a balanced distribution."""
    system_prompt = load_prompt("distribute")
    human_prompt = (
        f"Given:\n\n"
        f"agent_count = {agent_count}\n"
        f"item_dict = {json.dumps(item_dict, indent=4)}\n\n"
    )

    for attempt in range(max_retries + 1):
        try:
            response = call_with_messages(
                msgs=[
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=human_prompt)
                ],
                model_type=model_type,
                json_format=True
            )
            logger.debug(f"Resource distribution attempt {attempt + 1} response: {str(response.content)}")

            # Extract the JSON list from the response content
            agent_inventories = extract_json_list(response.content)

            # Validate the result
            if not isinstance(agent_inventories, list) or len(agent_inventories) != agent_count:
                raise ValueError("The LLM did not return a valid list of agent inventories.")

            for inventory in agent_inventories:
                if not isinstance(inventory, dict):
                    raise ValueError("Each element in the returned list should be a dictionary.")

            # Verify that the total sum of items matches the original item_dict
            combined_inventory = {}
            for inventory in agent_inventories:
                for item, count in inventory.items():
                    if item in combined_inventory:
                        combined_inventory[item] += count
                    else:
                        combined_inventory[item] = count

            if combined_inventory != item_dict:
                raise ValueError("The sum of all items across the agent_inventories does not match the original item_dict.")

            logger.success(f"Resource distribution successful on attempt {attempt + 1}.")
            # logger.info(f'Resource Distribution by {model_type}:', agent_inventories)
            return agent_inventories

        except (json.JSONDecodeError, ValueError) as e:
            logger.failed(f"Attempt {attempt + 1} failed: {e}")
            if attempt == max_retries:
                raise Exception("Failed to generate a valid resource distribution after maximum retries.")
            time.sleep(1)  # Wait a moment before retrying