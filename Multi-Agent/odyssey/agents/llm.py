import requests
from http import HTTPStatus
import json
import dashscope
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from pathlib import Path
from odyssey.utils import config
from openai import OpenAI

with open(Path(__file__).parent.parent.parent / "conf/config.json", "r") as config_file:
    config = json.load(config_file)

class ModelType:
    LLAMA2_70B = 'llama2_70b'
    LLAMA3_8B = 'llama3_8b'
    LLAMA3_70B = 'llama3_70b'
    DEEPSEEK = 'deepseek-chat'
    GPT = 'gpt'
    ALI = 'ali'

def call_with_messages(msgs, model_type:ModelType=ModelType.ALI, model_id=1, mode='text', input_url=None, openai_model='gpt-4o', deepseek_model='deepseek-chat', json_format=True, dashscope_model='qwen-plus', dashscope_vision_model='qwen-vl-plus'):
    if mode == 'text':
        apikey_messages =  [{'role': 'system', 'content': msgs[0].content},
                            {'role': 'user', 'content': msgs[1].content}]
    elif mode == 'vision':
        apikey_messages =  [{'role': 'system', 'content': msgs[0].content},
                            {'role': 'user', 'content': [{'type':'text', 'text':msgs[1].content}, {'type':'image_url', 'image_url':{'url':input_url}}]}]
    # use openai key
    if model_type == ModelType.GPT:
        openai_key = config.get('openai_key')
        client = OpenAI(api_key=openai_key)
        try:
            response = client.chat.completions.create(
                model=openai_model,
                messages=apikey_messages
            )
            return AIMessage(content=response.choices[0].message.content)
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
    # use deepseek key
    elif model_type == ModelType.DEEPSEEK:
        deepseek_key = config.get('deepseek_key')
        if json_format:
            client=OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com/beta")
            messages = [{'role': 'system', 'content': msgs[0].content},
                        {'role': 'user', 'content': msgs[1].content},
                        {'role': 'assistant', 'content': '```json\n', 'prefix':True}]
            try:
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=messages,
                    stop=["```"],
                )
                return AIMessage(content=response.choices[0].message.content)
            except Exception as e:
                print(f"Error calling deepseek API: {e}")
        else:
            client=OpenAI(api_key=deepseek_key, base_url="https://api.deepseek.com")
            try:
                response = client.chat.completions.create(
                    model=deepseek_model,
                    messages=apikey_messages
                )
                return AIMessage(content=response.choices[0].message.content)
            except Exception as e:
                print(f"Error calling deepseek API: {e}")
    # use alibaba key
    elif model_type == ModelType.ALI:
        client = OpenAI(
            api_key=config.get('dashscope_key'),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        try:
            response = client.chat.completions.create(
                model=dashscope_model if mode == 'text' else dashscope_vision_model,
                messages=apikey_messages
            )
            return AIMessage(content=response.choices[0].message.content)
        except Exception as e:
            print(f"Error calling AliCloud API: {e}")
    elif model_type in (ModelType.LLAMA3_8B, ModelType.LLAMA3_70B):
        # If no key is provided, call the LLMs on the server.
        url = f'http://{config.get("server_host")}:{config.get("server_port")}/{model_type}_{model_id}'
        input_msg = {
            "user_prompt": msgs[1].content,
            "system_prompt": msgs[0].content
        }
        result = requests.post(url, json = input_msg)
        # if result.status_code != HTTPStatus.OK:
        #     return AIMessage(content="")
        json_result = result.json()
        # if json_result['data'] is None:
        #     return AIMessage(content="")
        return AIMessage(content=json_result["data"])   

if __name__ == '__main__':
    import os
    import base64
    url = None
    image_path = os.path.join(os.getcwd(), f'memory/A/screen/Steve.png')
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
            base64_encoded = base64.b64encode(image_data).decode('utf-8')
            url = f'data:image/png;base64,{base64_encoded}'
    messages = [SystemMessage(content=f""), HumanMessage(content="You are a Minecraft gameplay assistant specialized in analyzing first-person perspective screenshots. Your task is to interpret the provided image and summarize the game environment reflected in the picture. This includes identifying the player's current location, surroundings, any nearby structures or landscapes, and the presence of any creatures or entities. Please provide a detailed description based on visual elements present in the image, considering both natural and built environments as well as dynamic elements such as animals, monsters, or other players if visible.You should respond in English and describe the player's environment in the second person, for example: 'You are currently standing in...' This approach will help create an immersive experience by directly addressing the player and their immediate surroundings. Be aware that the images may sometimes appear blurry, corrupted, or blank. In such cases, please ignore these anomalies and focus solely on identifying and describing Minecraft-related elements within the image. If the image is blank, just output something like 'You can't see your surroundings clearly'.")]
    res = call_with_messages(messages, mode='vision', input_url=url)
    print(res)
