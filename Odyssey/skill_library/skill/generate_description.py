import os
import http
import dashscope
import json
from odyssey.utils import config

dashscope.api_key = config.get('api_key')

def call_llama(js_content):
    """
    call LLAMA for description generation.

    Args:
        js_content: javascript code

    Returns:
        str: LLAMA response
    """
    system_message = """You are a helpful assistant that writes a description of the given function written in Mineflayer javascript code.
1) Focus on the implementation of the code, ignore anything related to chat messages! For example, don't include phrases like "send a chat message" in your description!
2) Do not mention the function name and anything about `bot.chat` or helper functions.
3) Try to summarize the function in no more than 6 sentences.
4) Your response should be a single line of text."""
    messages = [{'role': 'system', 'content': system_message},
                {'role': 'user', 'content': js_content}]

    response = dashscope.Generation.call(
        model='llama3-8b-instruct',
        # model='qwen1.5-72b-chat',
        messages=messages,
        result_format='message'
    )

    if response.status_code == http.HTTPStatus.OK:
        description = response["output"]["choices"][0]["message"]["content"]
        print("Generated Description:", description)
        return description
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))
        return None

def main(mode="all"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    code_dir = os.path.join(script_dir, "compositional")
    description_dir = os.path.join(script_dir, "description")

    for js_file in os.listdir(code_dir):
        if js_file.endswith(".js"):
            js_file_path = os.path.join(code_dir, js_file)
            description_file_path = os.path.join(description_dir, os.path.splitext(js_file)[0] + ".txt")

            if mode == "missing" and os.path.exists(description_file_path):
                print(f"Skipping {js_file} as description already exists")
                continue

            with open(js_file_path, 'r') as f:
                js_content = f.read()

            description = call_llama(js_content)

            if description:
                with open(description_file_path, 'w') as f:
                    f.write(description)
                    print(f"Description for {js_file} has been written to {description_file_path}")

if __name__ == "__main__":
    main(mode="missing")
    # mode "all" generates descriptions for all skills
    # mode "missing" generates descriptions for new skills
