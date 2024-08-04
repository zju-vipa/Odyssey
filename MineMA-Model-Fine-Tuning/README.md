# Model Fine-Tuning

Here, we have publicly disclosed the code used in the Model Fine-Tuning section of our research, along with publicly releasing our datasets and models.

## Training Dataset

The Minecraft QA-pairs Instruction Dataset used in our research has been publicly released on Huggingface, and you can access it at [https://huggingface.co/datasets/Aiwensile2/Minecraft_QA-pairs_Instruction_Dataset](https://huggingface.co/datasets/Aiwensile2/Minecraft_QA-pairs_Instruction_Dataset).

The code used to create this dataset is available in the "Training Dataset Generation" folder, specifically in the "training dataset generation code.py" file.

## Model Fine-Tuning

The MineMA-8B series of models and MineMA-70B series of models from our Minecraft domain knowledge expert series models MineMA, which were fine-tuned in our research, have been publicly released on Huggingface. You can access our models at [https://huggingface.co/Aiwensile2/MineMA-8B](https://huggingface.co/Aiwensile2/MineMA-8B).

The code used to fine-tune these models can be found in the "LoRA Fine-Tuning Codes" folder. Specifically, the "LLaMA2 Fine-tune code.py" and "LLaMA3 Fine-tune code.py" files correspond to the fine-tuning of the LLaMA-2 and LLaMA-3 series models, respectively.

## Model Evaluation

The evaluation datasets used in our research, the Multi-Theme MCQ Dataset and the Wiki-Based MCQ Dataset, have been made publicly available on Huggingface. You can access our datasets at [https://huggingface.co/datasets/Aiwensile2/Minecraft_MCQ_Datasets](https://huggingface.co/datasets/Aiwensile2/Minecraft_MCQ_Datasets).

The code used to create these datasets can be found in the "Evaluation Dataset Generation" folder. Specifically, the generation code for the Multi-Theme MCQ Dataset is in the file named "evaluation_dataset_v1 generation code.py" and the generation code for the Wiki-Based MCQ Dataset is in the file named "evaluation_dataset_v2 generation code.py".

The code used for the model evaluation process can be found in the "Evaluation Code" folder, within the file named "evaluation code.py".

## Model Usage

You can access our model, environment requirements, and usage instructions at [https://huggingface.co/Aiwensile2/MineMA-8B].

Or you can follow the steps below:

### 1. Model Download

Access our models at [https://huggingface.co/Aiwensile2/MineMA-8B]

### 2. Environment Setup

Environment requirements needed to use the model are written in "requirements.txt", which in the "Model Usage" folder.

Run the following command to install all dependencies:
```sh
pip install -r requirements.txt
```

### 3. Example Code

Example code for reference usage guidelines can be found at "Model Usage" folder, named "Model usage method.ipynb".

### 4. Prompts

We recommend using the following prompts:

System message: You are a Large Language Model, and your task is to answer questions posed by users about Minecraft. Utilize your knowledge and understanding of the game to provide detailed, accurate, and helpful responses. Use your capabilities to assist users in solving problems, understanding game mechanics, and enhancing their Minecraft experience.

User message: [A question about Minecraft]
