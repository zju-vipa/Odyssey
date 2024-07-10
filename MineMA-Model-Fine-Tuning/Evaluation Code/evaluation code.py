import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"   #You can modify the content here to suit your situation
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings
from tqdm import tqdm
warnings.filterwarnings("ignore")
model_id = ""  #You can modify the content here to suit your situation
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
csv_file = ""  #You can modify the content here to suit your situation, the dataset path has been specified here
df = pd.read_csv(csv_file)
questions = df['Q'].tolist()
answers = df['A'].tolist()

#You can modify the content below to suit your situation
sys_mes = "You are a Large Language Model, and your task is to answer questions posed by users about Minecraft. Utilize your knowledge and understanding of the game to provide detailed, accurate, and helpful responses. Use your capabilities to assist users in solving problems, understanding game mechanics, and enhancing their Minecraft experience."
correct_count = 0
results = []

def get_first_letter(answer):
    return answer.strip()[0].upper()

def contains_unique_option(model_output):
    options = ['A', 'B', 'C', 'D']
    extended_options = ['A.', 'B.', 'C.', 'D.']
    found_options = [opt for opt in options if opt in model_output]
    found_extended_options = [opt for opt in extended_options if opt in model_output]
    
    if len(found_options) == 1:
        return True, found_options[0]
    elif len(found_extended_options) == 1:
        return True, found_extended_options[0][0]
    else:
        return False, None

total_accuracy = 0

for run in range(1, 6):
    correct_count = 0
    results = []

    for question, correct_answer in tqdm(zip(questions, answers), total=len(questions), desc=f"Processing questions - Run {run}"):
        user_mes = f"""
        Based on your knowledge of Minecraft, please answer the following multiple-choice questions with only the option letter.
        {question}
        """

        messages = [
            {"role": "system", "content": sys_mes},
            {"role": "user", "content": user_mes},
        ]

        input_ids = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt"
        ).to(model.device)

        terminators = [
            tokenizer.eos_token_id,
            tokenizer.convert_tokens_to_ids("<|eot_id|>")  #if using LLama-2, then use 'tokenizer.convert_tokens_to_ids("</s>")' 
        ]

        #You can modify the content below to suit your situation
        outputs = model.generate(
            input_ids,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
        )
        
        response = outputs[0][input_ids.shape[-1]:]
        model_output = tokenizer.decode(response, skip_special_tokens=True).strip()
        model_answer_first_letter = get_first_letter(model_output)
        correct_answer_first_letter = get_first_letter(correct_answer)

        is_correct = False
        contains_unique, unique_option = contains_unique_option(model_output)
        if model_answer_first_letter == correct_answer_first_letter:
            is_correct = True
        elif contains_unique and unique_option == correct_answer_first_letter:
            is_correct = True

        if is_correct:
            correct_count += 1

        results.append({
            "Question": question,
            "Model Answer": model_output,
            "Correct Answer": correct_answer,
            "Is Correct": is_correct
        })

    accuracy = correct_count / len(questions)
    total_accuracy += accuracy

    results_df = pd.DataFrame(results)
    results_df.to_csv(f"{run}.csv", index=False)

    print(f"Run {run} accuracy: {accuracy * 100:.2f}%")
    
    #You can modify the content below to suit your situation, the result save path is specified here
    with open("", "a") as f:
        f.write(f"Run {run} accuracy: {accuracy * 100:.2f}%\n")

average_accuracy = total_accuracy / 5
#You can modify the content below to suit your situation, the result save path is specified here
with open("", "a") as f:
    f.write(f"Average accuracy: {average_accuracy * 100:.2f}%\n")

print(f"Average accuracy: {average_accuracy * 100:.2f}%")
