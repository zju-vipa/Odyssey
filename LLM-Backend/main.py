from api.api import create_app
from model.llama import Llama2, Llama3
from model.api_model import ModelFactory
import uvicorn
import os
from conf import config_manager

os.environ["CUDA_VISIBLE_DEVICES"] = config_manager.get('CUDA_VISIBLE_DEVICES')

if __name__ == "__main__":
    models_path = config_manager.get('models')
    cuda_visible_devices = config_manager.get('CUDA_VISIBLE_DEVICES')
    if len(cuda_visible_devices.split(',')) == 1:
        device_map = {"": int(cuda_visible_devices)}
    else:
        device_map = "auto"
    models = {}
    for name in models_path:
        if name.startswith('llama3'):
            models[name] = Llama3(model_path=models_path[name], device_map=device_map)
        elif name.startswith('llama2'):
            models[name] = Llama2(model_path=models_path[name], device_map=device_map)
    models['qwen2-7b'] = lambda system_prompt, user_prompt: ModelFactory.call('qwen2-7b', messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}])
    models['qwen2-72b'] = lambda system_prompt, user_prompt: ModelFactory.call('qwen2-72b', messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}])
    models['baichuan2-7b'] = lambda system_prompt, user_prompt: ModelFactory.call('baichuan2-7b', messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': user_prompt}])
    app = create_app(models)
    uvicorn.run(app, host="0.0.0.0", port=config_manager.get('port'))

