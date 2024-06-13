


from api.api import create_app
from model.llama import Llama2, Llama3
import uvicorn
import os
from conf import config_manager
os.environ["CUDA_VISIBLE_DEVICES"] = config_manager.get('CUDA_VISIBLE_DEVICES') #指定cuda可见显卡编号
if __name__ == "__main__":
    models_path = config_manager.get('models')
    models = {}
    for name in models_path:
        if name.startswith('llama3'):
            models[name] = Llama3(model_path=models_path[name], device_map="auto")
        elif name.startswith('llama2'):
            models[name] = Llama2(model_path=models_path[name], device_map="auto")
    app = create_app(models)
    uvicorn.run(app, host="0.0.0.0", port=config_manager.get('port'))