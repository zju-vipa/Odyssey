# Import environment
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # You can modify the content here to suit your situation
from datasets import Dataset
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer, GenerationConfig
import transformers
import torch
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
    EarlyStoppingCallback,
)

# Import the dataset, split into training and testing datasets
df = pd.read_json('')
train_df_three = df.sample(frac=0.95, random_state=123)  # You can modify the content here to suit your situation
test_df_three = df.drop(train_df_three.index)
ds = Dataset.from_pandas(train_df_three)
ds_test = Dataset.from_pandas(test_df_three)

# Import the base model
tokenizer = AutoTokenizer.from_pretrained('', use_fast=False, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained('', device_map="auto",torch_dtype=torch.bfloat16)
model.enable_input_require_grads()

def process_func(example):
    MAX_LENGTH = 1024
    input_ids, attention_mask, labels = [], [], []
    instruction = tokenizer(f"<|start_header_id|>system<|end_header_id|>\n\nYou are a Large Language Model, and your task is to answer questions posed by users about Minecraft. Utilize your knowledge and understanding of the game to provide detailed, accurate, and helpful responses. Use your capabilities to assist users in solving problems, understanding game mechanics, and enhancing their Minecraft experience.<|start_header_id|>user<|end_header_id|>\n\n{example['instruction']}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n", add_special_tokens=False) 
    response = tokenizer(f"{example['output']}<|eot_id|>", add_special_tokens=False)
    input_ids = instruction["input_ids"] + response["input_ids"] + [tokenizer.pad_token_id]
    attention_mask = instruction["attention_mask"] + response["attention_mask"] + [1] 
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"] + [tokenizer.pad_token_id]  
    if len(input_ids) > MAX_LENGTH: 
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

tokenized_id = ds.map(process_func, remove_columns=ds.column_names)
tokenized_id_test = ds_test.map(process_func, remove_columns=ds_test.column_names)

# LoRA parameter settings, you can modify the content below to suit your situation
config = LoraConfig(
    task_type=TaskType.CAUSAL_LM, 
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    inference_mode=False,
    r=32, 
    lora_alpha=64, 
    lora_dropout=0.1
)

model = get_peft_model(model, config)

# Set training parameters, you can modify the content below to suit your situation
args = TrainingArguments(
    output_dir="",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,
    logging_steps=50,
    num_train_epochs=5,
    save_steps=100,
    learning_rate=1e-4,
    save_on_each_node=False,
    gradient_checkpointing=True,
    eval_steps=100,
    weight_decay=1e-4,
    load_best_model_at_end=True,
    evaluation_strategy="steps"
)
callbacks = [EarlyStoppingCallback(early_stopping_patience=5)]
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized_id,
    eval_dataset=tokenized_id_test,
    data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer, padding=True),
    callbacks=callbacks,
)

trainer.train()
save_path=""
trainer.model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

# Merge models, you can choose whether to merge the LoRA model with the base model
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from peft import PeftModel
from peft import LoraConfig, TaskType, get_peft_model

config = LoraConfig(
    task_type=TaskType.CAUSAL_LM, 
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    inference_mode=False, 
    r=16,
    lora_alpha=32,
    lora_dropout=0.1
)
new_model_path = ""
lora_model_path = ""
base_model_path = ""

base_model = AutoModelForCausalLM.from_pretrained(base_model_path, device_map="auto",torch_dtype=torch.bfloat16)
model = PeftModel.from_pretrained(base_model, lora_model_path, config=config)
model = model.merge_and_unload()
tokenizer = AutoTokenizer.from_pretrained(base_model_path, trust_remote_code=True)

model.save_pretrained(new_model_path)
tokenizer.save_pretrained(new_model_path)
"""