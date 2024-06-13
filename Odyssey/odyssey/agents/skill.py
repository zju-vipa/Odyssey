import os

import odyssey.utils as U
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.schema import HumanMessage, SystemMessage
from langchain.vectorstores import Chroma

from odyssey.prompts import load_prompt
from odyssey.control_primitives import load_control_primitives
from odyssey.utils.logger import get_logger

class SkillManager:
    def __init__(
        self,
        retrieval_top_k=5,
        request_timout=120,
        ckpt_dir="ckpt",
        resume=False,
        reload=False,
        embedding_model="",
    ):
        U.f_mkdir(f"{ckpt_dir}/skill/compositional")
        U.f_mkdir(f"{ckpt_dir}/skill/description")
        U.f_mkdir(f"{ckpt_dir}/skill/vectordb")
        if reload:
            U.f_remove(f"{ckpt_dir}/skill/vectordb")
        # programs for env execution
        self.control_primitives = load_control_primitives()
        self.skill_primitives = self.load_skill_primitives()
        self.logger = get_logger("SkillManager")
        if resume:
            self.skills = U.load_json(f"{ckpt_dir}/skill/skills.json")
            self.logger.info(f"Loading {len(self.skills)} skills from {ckpt_dir}/skill")
        else:
            self.skills = {}
        self.retrieval_top_k = retrieval_top_k
        self.ckpt_dir = ckpt_dir
        self.vectordb = Chroma(
            collection_name="skill_vectordb",
            embedding_function=HuggingFaceEmbeddings(model_name=embedding_model),
            persist_directory=f"{ckpt_dir}/skill/vectordb",
        )
        if reload:
            for key, value in self.skills.items():
                self.vectordb.add_texts(
                    texts=[value['description']],
                    ids=[key],
                    metadatas=[{"name": key}],
                )
            
            self.vectordb.persist()
        
        assert self.vectordb._collection.count() == len(self.skills), (
            f"Skill Manager's vectordb is not synced with skills.json.\n"
            f"There are {self.vectordb._collection.count()} skills in vectordb but {len(self.skills)} skills in skills.json.\n"
            f"Did you set resume=False when initializing the manager?\n"
            f"You may need to manually delete the vectordb directory for running from scratch."
        )

    @property
    def programs(self):
        programs = ""
        for skill_name, entry in self.skills.items():
            programs += f"{entry['code']}\n\n"
        for primitives in self.control_primitives:
            programs += f"{primitives}\n\n"
        for skill_primitive in self.skill_primitives:
            programs += f"{skill_primitive}\n\n"
        return programs

    def add_new_skill(self, info):
        if info["task"].startswith("Deposit useless items into the chest at"):
            # No need to reuse the deposit skill
            return
        program_name = info["program_name"]
        program_code = info["program_code"]
        skill_description = self.generate_skill_description(program_name, program_code)
        self.logger.info(f"Skill Manager generated description for {program_name}:\n{skill_description}")
        if program_name in self.skills:
            self.logger.warning(f"Skill {program_name} already exists. Rewriting!")
            self.vectordb._collection.delete(ids=[program_name])
            i = 2
            while f"{program_name}V{i}.js" in os.listdir(f"{self.ckpt_dir}/skill/compositional"):
                i += 1
            dumped_program_name = f"{program_name}V{i}"
        else:
            dumped_program_name = program_name
        self.vectordb.add_texts(
            texts=[skill_description],
            ids=[program_name],
            metadatas=[{"name": program_name}],
        )
        self.skills[program_name] = {
            "code": program_code,
            "description": skill_description,
        }
        assert self.vectordb._collection.count() == len(
            self.skills
        ), "vectordb is not synced with skills.json"
        U.dump_text(
            program_code, f"{self.ckpt_dir}/skill/compositional/{dumped_program_name}.js"
        )
        U.dump_text(
            skill_description,
            f"{self.ckpt_dir}/skill/description/{dumped_program_name}.txt",
        )
        U.dump_json(self.skills, f"{self.ckpt_dir}/skill/skills.json")
        self.vectordb.persist()

    def generate_skill_description(self, program_name, program_code):
        messages = [
            SystemMessage(content=load_prompt("skill")),
            HumanMessage(
                content=program_code
                + "\n\n"
                + f"The main function is `{program_name}`."
            ),
        ]
        skill_description = f"    // { self.llm(messages).content}"
        return f"async function {program_name}(bot) {{\n{skill_description}\n}}"

    def retrieve_skills(self, query):
        k = min(self.vectordb._collection.count(), self.retrieval_top_k)
        if k == 0:
            return []
        self.logger.info(f"Skill Manager retrieving for {k} skills")
        docs_and_scores = self.vectordb.similarity_search_with_score(query, k=k)
        self.logger.debug(
            f"Skill Manager retrieved skills: "
            f"{', '.join([doc.metadata['name'] for doc, _ in docs_and_scores])}"
        )
        self.logger.debug(
            f"Skill Manager retrieved skills Scores: "
            f"{[score for _, score in docs_and_scores]}"
        )

        code = []
        description = []
        for doc, _ in docs_and_scores:
            code.append(self.skills[doc.metadata["name"]]["code"])
            description.append(self.skills[doc.metadata["name"]]["description"])
        
        skills = [code, description]
        # print(skills)
        return skills

    def load_skill_primitives(self, primitive_names=None):
        package_path = "skill_library/skill"
        if primitive_names is None:
            primitive_names = [
                primitives[:-3]
                for primitives in os.listdir(f"{package_path}/primitive")
                if primitives.endswith(".js")
            ]
        primitives = [
            U.load_text(f"{package_path}/primitive/{primitive_name}.js")
            for primitive_name in primitive_names
        ]
        return primitives