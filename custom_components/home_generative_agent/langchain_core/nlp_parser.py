import json
from pathlib import Path
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama

class NLPParser:
    def __init__(self, config_path: str):
        config = Path(config_path).read_text()
        self.prompt = PromptTemplate.from_template(config)
        self.llm = Ollama(model="llama3", base_url="http://192.168.72.128:11434")


    def parse(self, instruction: str) -> dict:
        formatted = self.prompt.format(instruction=instruction)
        response = self.llm.invoke(formatted)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"action": "unknown", "target": ""}
