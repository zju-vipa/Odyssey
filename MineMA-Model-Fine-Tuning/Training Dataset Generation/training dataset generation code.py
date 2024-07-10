import os
import random
from openai import OpenAI
import pandas as pd

#You can modify the content below to suit your situation
client = OpenAI(
    api_key='',
    base_url=''
)

def normal_answer(user_content):
  try:
    response0 = client.chat.completions.create(
      model="",  #You can modify the content here to suit your situation
      messages=[
          {
              "role": "system",
              "content": f"You are a question-and-answer dataset generating expert, you are generating data that will be used to train a large language model designed to address questions posed by users regarding the game Minecraft, and from that, you will generate question-and-answer data samples, each with a prompt/response pair.\n\nYou will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n\nYour task is to generate at least 20 examples.Make sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model."
          },
          {
              "role": "user",
              "content":"Your task is to generate 20 question-and-answer examples. And you will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n. Please generate as many question and answer pairs as possible. Here are the user content:"+user_content
          }
      ],
      stream=False,
    )
    return response0.choices[0].message.content
  except Exception as e:
    print(f"Error processing file due to: {e}")
    return None
def short_answer(user_content):
  try:
    response1 = client.chat.completions.create(
      model="",  #You can modify the content below to suit your situation
      messages=[
          {
              "role": "system",
              "content": f"You are a question-and-answer dataset generating expert, you are generating data that will be used to train a large language model designed to address questions posed by users regarding the game Minecraft, and from that, you will generate question-and-answer data samples, each with a prompt/response pair.\n\nYou will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n\nYour task is to generate at least 30 examples.Make sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model."
          },
          {
              "role": "user",
              "content":"Your task is to generate 30 question-and-answer examples, and you should generate questions within the provided user text that can be directly answered with a word or phrase, such as dates, names, statistics, etc. This involves identifying specific, concise information within the text that can be succinctly responded to, ensuring that the answers are clear and directly related to the questions asked. And you will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n. Please generate as many question and answer pairs as possible. Here are the user content:"+user_content
          }
      ],
      stream=False,
    )
    return response1.choices[0].message.content
  except Exception as e:
    print(f"Error processing file due to: {e}")
    return None
def long_answer(user_content):
  try:
    response2 = client.chat.completions.create(
      model="",  #You can modify the content below to suit your situation
      messages=[
          {
              "role": "system",
              "content": f"You are a question-and-answer dataset generating expert, you are generating data that will be used to train a large language model designed to address questions posed by users regarding the game Minecraft, and from that, you will generate question-and-answer data samples, each with a prompt/response pair.\n\nYou will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n\nYour task is to generate at least 20 examples.Make sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model."
          },
          {
              "role": "user",
              "content":"Your task is to generate 20 question-and-answer examples. Identify questions within the provided user text that require one or more complete sentences as answers. These questions should be suitable for explanatory or definitional responses, where a detailed explanation or a clear definition is needed to fully address the question. This involves crafting answers that are comprehensive and informative, ensuring they adequately explain or define the subject matter in question. And you will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n. Please generate as many question and answer pairs as possible. Here are the user content:"+user_content
          }
      ],
      stream=False,
    )
    return response2.choices[0].message.content
  except Exception as e:
    print(f"Error processing file due to: {e}")
    return None
def bool_answer(user_content):
  try:
    response3 = client.chat.completions.create(
      model="",  #You can modify the content below to suit your situation
      messages=[
          {
              "role": "system",
              "content": f"You are a question-and-answer dataset generating expert, you are generating data that will be used to train a large language model designed to address questions posed by users regarding the game Minecraft, and from that, you will generate question-and-answer data samples, each with a prompt/response pair.\n\nYou will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n\nYour task is to generate at least 10 examples.Make sure your samples are unique and diverse, yet high-quality and complex enough to train a well-performing model."
          },
          {
              "role": "user",
              "content":"Your task is to generate 10 question-and-answer examples. Look for questions within the provided user text that can be answered with a simple True or False. This task involves pinpointing statements or queries within the text that lend themselves to binary responses, ensuring that the answers are straightforward and unambiguous, clearly indicating whether the statement is true or false based on the information available. And you will do so in this format:\n```\nprompt\n-----------\n$prompt_goes_here\n-----------\n\nresponse\n-----------\n$response_goes_here\n-----------\n```\n. Please generate as many question and answer pairs as possible. Here are the user content:"+user_content
          }
      ],
      stream=False,
    )
    return response3.choices[0].message.content
  except Exception as e:
    print(f"Error processing file due to: {e}")
    return None
def normal_read_md_files(folder_path, start_from=0):
    if not os.path.exists(folder_path):
        print("The given path does not exist")
        return
    count = 0
    file_number = 0
    csv_number = 1
    save_path = ''
    prompts = []
    responses = []
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    md_files.sort()
    for filename in md_files:
        file_number += 1
        if file_number < start_from:
          continue

        file_path = os.path.join(folder_path, filename)

        print(f"Reading: {file_path}")  #You can omit the "print" in this section and the following sections
        with open(file_path, 'r') as file:
            data = file.read()
        re0 = normal_answer(data)
        if re0 is None:
          print(f"An error in {file_path}")
          count += 1
          continue
        split_example0 = re0.split('-----------')
        length0 = len(split_example0)
        retry=0
        flag=1
        while (length0 < 20 and retry < 3) or flag == 0:   #You can modify the content here to suit your situation
          flag=1
          re0 = normal_answer(data)
          if re0 is None:
            print(f"An error in {file_path}")
            retry += 1
            continue
          split_example0 = re0.split('-----------')
          length0 = len(split_example0)
          retry += 1
          for i in range(1,length0//4+1):
            if 'prompt' in split_example0[4*i-3].strip() or 'response' in split_example0[4*i-3].strip() or 'prompt' in split_example0[4*i-1].strip() or 'response' in split_example0[4*i-1].strip():
              flag = 0
              break
        for i in range(1,length0//4+1):
          prompts.append(split_example0[4*i-3].strip())
          responses.append(split_example0[4*i-1].strip())
        if count % 100 == 99:
          df = pd.DataFrame({
                'prompt': prompts,
                'response': responses
          })
          df = df.drop_duplicates()
          csv_filename = f'normal_crawler_data_{csv_number}.csv'
          df.to_csv(os.path.join(save_path, csv_filename), index=False)
          prompts, responses = [], []
          print(f"{csv_number} datasets have been saved.")
          csv_number += 1
        count += 1
        print(f"Read {count} files. Current file number: {file_number}, path: {file_path}")

def three_read_md_files(folder_path, start_from=0):
    if not os.path.exists(folder_path):
        print("The given path does not exist")
        return
    count = 0
    file_number = 0
    csv_number = 1
    save_path = ''
    prompts = []
    responses = []
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
    md_files.sort()
    for filename in md_files:
        file_number += 1
        if file_number < start_from:
          continue

        file_path = os.path.join(folder_path, filename)

        print(f"Reading:{file_path}")
        with open(file_path, 'r') as file:
            data = file.read()
        re1 = short_answer(data)
        if re1 is None:
          print(f"An error in {file_path}")
          with open('', 'a') as log_file:
            log_file.write(filename + '\n')
          count += 1
          continue
        split_example1 = re1.split('-----------')
        length1 = len(split_example1)
        retry=0
        flag=1
        while (length1 < 20 and retry < 3) or flag == 0:   #You can modify the content here to suit your situation
          flag=1
          re1 = short_answer(data)
          if re1 is None:
            print(f"An error in {file_path}")
            retry += 1
            continue
          split_example1 = re1.split('-----------')
          length1 = len(split_example1)
          retry += 1
          for i in range(1,length1//4+1):
            if 'prompt' in split_example1[4*i-3].strip() or 'response' in split_example1[4*i-3].strip() or 'prompt' in split_example1[4*i-1].strip() or 'response' in split_example1[4*i-1].strip():
              flag = 0
              break
        for i in range(1,length1//4+1):
          prompts.append(split_example1[4*i-3].strip())
          responses.append(split_example1[4*i-1].strip())
        re2 = long_answer(data)
        if re2 is None:
          print(f"An error in {file_path}")
          count += 1
          continue
        split_example2 = re2.split('-----------')
        length2 = len(split_example2)
        retry=0
        flag=1
        while (length2 < 20 and retry < 3) or flag == 0:   #You can modify the content here to suit your situation
          flag=1
          re2 = long_answer(data)
          if re2 is None:
            print(f"An error in {file_path}")
            retry += 1
            continue
          split_example2 = re2.split('-----------')
          length2 = len(split_example2)
          retry += 1
          for i in range(1,length2//4+1):
            if 'prompt' in split_example2[4*i-3].strip() or 'response' in split_example2[4*i-3].strip() or 'prompt' in split_example2[4*i-1].strip() or 'response' in split_example2[4*i-1].strip():
              flag = 0
              break
        for i in range(1,length2//4+1):
          prompts.append(split_example2[4*i-3].strip())
          responses.append(split_example2[4*i-1].strip())
        re3 = bool_answer(data)
        if re3 is None:
          print(f"An error in {file_path}")
          count += 1
          continue
        split_example3 = re3.split('-----------')
        length3 = len(split_example3)
        retry=0
        flag=1
        while (length3 < 16 and retry < 3) or flag == 0:   #You can modify the content here to suit your situation
          flag=1
          re3 = bool_answer(data)
          if re3 is None:
            print(f"An error in {file_path}")
            retry += 1
            continue
          split_example3 = re3.split('-----------')
          length3 = len(split_example3)
          retry += 1
          for i in range(1,length3//4+1):
            if 'prompt' in split_example3[4*i-3].strip() or 'response' in split_example3[4*i-3].strip() or 'prompt' in split_example3[4*i-1].strip() or 'response' in split_example3[4*i-1].strip():
              flag = 0
              break
        for i in range(1,length3//4+1):
          prompts.append(split_example3[4*i-3].strip())
          responses.append(split_example3[4*i-1].strip())
        if count % 100 == 99:
          df = pd.DataFrame({
            'prompt': prompts,
            'response': responses
          })
          df = df.drop_duplicates()
          csv_filename = f'three_crawler_data_{csv_number}.csv'
          df.to_csv(os.path.join(save_path, csv_filename), index=False)
          prompts, responses = [], []
          print(f"{csv_number} datasets have been saved.")
          csv_number += 1
        count += 1
        print(f"Read {count} files. Current file number: {file_number}, path: {file_path}")

folder_path = ''  #You can modify the content here to suit your situation
start_from = 1
normal_read_md_files(folder_path, 1)
three_read_md_files(folder_path, 1)

