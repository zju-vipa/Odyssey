import random
from http import HTTPStatus
from dashscope import Generation
import dashscope

dashscope.api_key = "sk-xxx"

class ModelFactory:
    models = {
        'qwen2-7b': 'qwen2-7b-instruct',
        'qwen2-72b': 'qwen2-72b-instruct',
        'baichuan2-7b': 'baichuan2-7b-chat-v1',
    }

    @classmethod
    def call(cls, model_name, messages):
        if model_name in cls.models:
            model = cls.models[model_name]
            response = Generation.call(model=model,
                                       messages=messages,
                                       seed=random.randint(1, 10000),
                                       temperature=0.6,
                                       top_p=0.9,
                                       max_tokens=256,
                                       result_format='message')
            content =  response["output"]["choices"][0]["message"]["content"]
            return content
        else:
            raise ValueError(f"Unsupported model '{model_name}'")