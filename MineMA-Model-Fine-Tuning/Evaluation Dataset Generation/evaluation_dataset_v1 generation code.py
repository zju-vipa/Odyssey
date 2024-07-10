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
    sys_mes_g = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "Game Basics" and the provided keywords. The introduction of the theme of "Game Basics" is as follows:

Game Basics:
Blocks and Items: Basic blocks, special blocks, tools, weapons, armor, etc.
Survival Mechanics: Health, hunger, experience levels, death and respawn, etc.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: Game Basics
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""
    sys_mes_w = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "World Exploration" and the provided keywords. The introduction of the theme of "World Exploration" is as follows:

World Exploration:
Biomes: Characteristics of different biomes, generated structures, unique resources, etc.
Terrain and Landforms: Features and resource distribution of different terrains.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: World Exploration
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""
    sys_mes_m = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "Mobs and Interactions" and the provided keywords. The introduction of the theme of "Mobs and Interactions" is as follows:

Mobs and Interactions:
Mobs: Characteristics and behaviors of passive, neutral, and hostile mobs.
Combat System: Monster types, combat tactics, weapons and equipment, enchantments, potions, etc.
Trading and Villagers: Villager professions, trading mechanics, village structures, etc.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: Mobs and Interactions
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""
    sys_mes_sur = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "Survival Skills" and the provided keywords. The introduction of the theme of "Survival Skills" is as follows:

Survival Skills:
Resource Gathering: Methods of obtaining various resources and their uses.
Crafting and Production: Usage of crafting tables, furnaces, etc., equipment crafting and upgrading.
Farming and Animal Husbandry: Crop planting, animal breeding, automated farms, etc.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: Survival Skills
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""
    sys_mes_b = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "Building and Creativity" and the provided keywords. The introduction of the theme of "Building and Creativity" is as follows:

Building and Creativity:
Building Styles: Various building styles and key points.
Building Techniques: Symmetry, proportion, detail handling in construction, etc.
Interior Decoration: Interior design, lighting, item placement, etc.
Redstone Mechanics: Redstone components, circuit design, automated devices, etc.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: Building and Creativity
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""
    sys_mes_sp = """You are an expert in generating Minecraft quiz questions. Your task is to create multiple-choice questions about the game Minecraft based on the theme of "Special Dimensions" and the provided keywords. The introduction of the theme of "Special Dimensions" is as follows:

Special Dimensions:
The Nether: Peculiarities of the Nether, unique blocks and mobs, special structures, etc.
The End: Characteristics of the End, Ender Dragon, cities, ships, etc.
Adventure and Exploration: Special generated structures like ocean monuments, woodland mansions, ruins, fortresses, etc.

Provide four answer options labeled A, B, C, and D. Only one option should be correct. After the question and options, state the correct answer. Please format the output as follows:

Difficulty: Easy/Medium/Hard
Topic: Special Dimensions
Key Word: text
Question: Question text
Options: A.text B.text C.text D.text
Correct Answer: A/B/C/D

Ensure that the difficulty distribution of the questions and options is reasonable, and the answers should be detailed and informative.
"""

    user_mes1 = """Please generate some Minecraft multiple-choice questions based on the following 5 keywords, covering three difficulty levels: simple, moderate, and difficult. The number after the keyword represents how many multiple-choice questions to generate based on this keyword.

Keywords:

"""
    user_mes2 = """Ensure that the Q&A content is rich and accurate, and test the player's understanding of the game. Provide a balanced combination of simple, medium, and difficult questions. Generate each question and answer in the given format. Here is an example:

Example:

"""
    user_mes = user_mes1 + c1 + "\n\n"+ user_mes2 + c2
    print(user_mes)
    response0 = client.chat.completions.create(
      model="", #You can modify the content here to suit your situation
      messages=[
          {
              "role": "system",
              "content": sys_mes_sp
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
    t2 = """Difficulty: Hard
Topic: Special Dimensions
Key Word: End Ship
Question: What exclusive item can be found in the End Ship in Minecraft?
Options: A. Netherite B. Dragon Egg C. Elytra D. Beacon
Correct Answer: C
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
        question_and_options = "\n".join(lines[3:5])


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
    with open(file_path, 'r') as file:
        for line in file:
            processed_line = line.split(' ', 1)[1]
            batch += processed_line
            count += 1
            if count == batch_size:
                process_batch(batch)
                batch = ""
                count = 0
        if batch:
            process_batch(batch)

read_batches_from_file('')  #You can modify the content here to suit your situation

