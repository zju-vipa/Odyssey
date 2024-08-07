import os
import torch
from typing import Union
from pathlib import Path
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)

class Llama2:
    use_4bit = True
    bnb_4bit_compute_dtype = "float16"
    bnb_4bit_quant_type = "nf4"
    use_nested_quant = False

    def __init__(self, model_path: Path, max_length:int =1024, device_map: Union[dict,str]='',
                 repetition_penalty:float = 1.18, no_repeat_ngram_size:int = 5,
                 return_full_text:bool = False, temperature: float = 0.8) -> None:
        self.compute_dtype = getattr(torch, self.bnb_4bit_compute_dtype)
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=self.use_4bit,
            bnb_4bit_quant_type=self.bnb_4bit_quant_type,
            bnb_4bit_compute_dtype=self.compute_dtype,
            bnb_4bit_use_double_quant=self.use_nested_quant,
        )
        self.model = AutoModelForCausalLM.from_pretrained(model_path,
                                                          quantization_config=bnb_config,
                                                          device_map='auto') 
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.pipeline = pipeline(
                                    task="text-generation", 
                                    model=self.model, 
                                    tokenizer=self.tokenizer,
                                    max_length=max_length,
                                    # repetition_penalty=repetition_penalty,
                                    # no_repeat_ngram_size=no_repeat_ngram_size,
                                    return_full_text=return_full_text,
                                    temperature=temperature
                                )
        
        

    def __call__(self, system_prompt: str, user_prompt: str) -> str:
        prompttext = f'[INST]<<SYS>>\n{system_prompt}\n<</SYS>>\n\n {user_prompt} \n[/INST]' 
        print('==='*30)
        print(prompttext)
        print('---'*30)
        resp = self.pipeline(prompttext)
        if len(resp) > 0:
            resp = resp[0]
            resp = resp.get('generated_text', None)
            print(resp)
            print('==='*30)
            return resp
        else:
            print('==='*30)
            return None
    
class Llama3:
    def __init__(self, model_path: Path, device_map: Union[dict,str]='',max_new_tokens:int=256,do_sample:bool=True,temperature:float=0.6,top_p:float=0.9):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.bfloat16,
            device_map = device_map,
        )
        self.max_new_tokens = max_new_tokens
        self.do_sample= do_sample
        self.temperature = temperature
        self.top_p = top_p
    
    def __call__(self, system_prompt: str, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        input_ids = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(self.model.device)

        terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = self.model.generate(
            input_ids,
            max_new_tokens=self.max_new_tokens,
            eos_token_id=terminators,
            do_sample=self.do_sample,
            temperature=self.temperature,
            top_p=self.top_p,
            # pad_token_id=self.tokenizer.eos_token_id,
            # repetition_penalty=1.3, 
        )
        if len(outputs) > 0:
            response = outputs[0][input_ids.shape[-1]:]
            return self.tokenizer.decode(response, skip_special_tokens=True)
        else:
            return None
        
    
if __name__ == '__main__':
    model = Llama('/path/to/your/llama3_xxxx.weights')
