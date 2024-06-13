
from typing import Union

from fastapi import FastAPI, Request
from pydantic import BaseModel
from entity.llama import LlamaRequest, LlamaResponse
import asyncio
semaphore = asyncio.Semaphore(18)
concurrent_requests = 0
def create_app(models)->FastAPI:
    app = FastAPI()

    @app.get("/ping")
    def ping():
        return {"data": "pong!"}
    @app.get("/status")
    def status():
        return {"concurrent_requests": concurrent_requests}
    @app.middleware("http")
    async def record_concurrent_requests(request: Request, call_next):
        global concurrent_requests
        try:
            concurrent_requests += 1
            response = await call_next(request)
            return response
        finally:
            concurrent_requests -= 1
            
    def create_route(model_name):
        @app.post(f"/{model_name}", response_model=LlamaResponse)
        async def llama(llama_request: LlamaRequest):
            async with semaphore:
                response = models[model_name](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
                return {"status": 0, "data": response}
        
    for name in models.keys():
        create_route(name)
        
    # @app.post("/llama", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['v1'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    
    # @app.post("/llama2_70b", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama2_70b'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    
    # @app.post("/llama3_70b", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama3_70b'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    
    # @app.post("/llama3_8b", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama3_8b'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    
    # @app.post("/llama2", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama2'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    
    # @app.post("/llama2_13b_v3", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama2_13b_v3'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}

    # @app.post("/llama2_13b_v4", response_model=LlamaResponse)
    # def llama(llama_request: LlamaRequest):
    #     response = models['llama2_13b_v4'](user_prompt=llama_request.user_prompt, system_prompt=llama_request.system_prompt)
    #     return {"status": 0, "data": response}
    return app