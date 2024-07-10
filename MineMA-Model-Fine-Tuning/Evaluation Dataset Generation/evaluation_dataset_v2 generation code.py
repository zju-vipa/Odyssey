import os
import random
from openai import OpenAI
import pandas as pd

#You can modify the content below to suit your situation
client = OpenAI(
    api_key='',
    base_url=''
)


def normal_answer(c1,c2):
  try:
    sys_mes = """You are an expert in generating Minecraft multiple-choice questions. Your task is to create multiple choice questions about the game Minecraft based on the provided keywords and the information on the corresponding page on the Minecraft Wiki. Ensure that the source of information for the multiple-choice questions you generate is the Minecraft Wiki, while ensuring the objectivity and accuracy of the multiple-choice questions and ensuring good quality.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Do not use '#' or '*'.

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""

    user_mes1 = """Please generate some Minecraft multiple-choice questions based on the following 5 keywords, covering three difficulty levels: simple, moderate, and difficult. The number after the keyword represents the minimum number of multiple-choice questions generated based on the keyword. For important keyword, you should generate more questions.

Keywords:

"""
    user_mes2 = """Ensure the source of information for the multiple-choice questions you generate is the Minecraft Wiki, while ensuring the objectivity and accuracy of the multiple-choice questions and ensuring good quality. Provide a balanced combination of simple, medium, and difficult questions. Generate each question and answer in the given format, do not use '#' or '*'.. Here is an example:

Example:

"""
    user_mes = user_mes1 + c1 + "\n\n"+ user_mes2 + c2
    response0 = client.chat.completions.create(
      model="",  #You can modify the content here to suit your situation
      messages=[
          {
              "role": "system",
              "content": sys_mes
          },
          {
              "role": "user",
              "content": user_mes
          }
      ],
      stream=False,
    )
    return response0.choices[0].message.content
  except Exception as e:
    print(f"Error processing file due to: {e}")
    return None


def process_batch(batch):
    t2 = """Difficulty: Medium
Key Word: Dirt
Question: What happens when you right-click on a dirt block with a hoe?
Options:
A. It turns into farmland
B. It turns into grass
C. It turns into a path block
D. Nothing happens
Correct Answer: A
"""
    flag = 0
    while flag == 0:
      flag = 1
      ans = normal_answer(batch,t2)
      if ans is None:
        flag = 0
    question_blocks = ans.split("\n\n")
    with open('', 'a') as file:
        file.write('\n\n' + ans)

    df = pd.DataFrame(columns=['question message', 'Q', 'A'])
    data_rows = []

    for block in question_blocks:
        lines = block.split('\n')
        correct_answer = lines[-1].split(': ')[-1]
        question_and_options = "\n".join(lines[2:8])


        data_rows.append({
            'question message': block,
            'Q': question_and_options,
            'A': correct_answer
        })

    df = pd.DataFrame(data_rows)
    csv_file_path = ''  #You can modify the content here to suit your situation
    json_file_path = ''  #You can modify the content here to suit your situation

    if os.path.exists(csv_file_path):
        existing_csv_df = pd.read_csv(csv_file_path)
        combined_csv_df = pd.concat([existing_csv_df, df], ignore_index=True)
    else:
        combined_csv_df = df

    if os.path.exists(json_file_path):
        existing_json_df = pd.read_json(json_file_path)
        combined_json_df = pd.concat([existing_json_df, df], ignore_index=True)
    else:
        combined_json_df = df

    combined_csv_df.to_csv(csv_file_path, index=False)
    combined_json_df.to_json(json_file_path, orient='records')


def read_batches_from_file(file_path):
    batch_size = 5
    count = 0
    batch = ""
    cnum = 0
    with open(file_path, 'r') as file:
        for line in file:
            processed_line = line.split(' ', 1)[1]
            batch += processed_line
            count += 1
            if count == batch_size:
                cnum += 1
                print(cnum)
                process_batch(batch)
                batch = ""
                count = 0
        if batch:
            process_batch(batch)

read_batches_from_file('')  #You can modify the content here to suit your situation

