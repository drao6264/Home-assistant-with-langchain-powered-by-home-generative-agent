from .nlp_parser import NLPParser
from .ha_client import HAAPI

class AssistantCommandHandler:
    def __init__(self, config_path: str, ha_token: str, ha_url: str):
        self.parser = NLPParser(config_path)
        self.ha_client = HAAPI(ha_token, ha_url)

    def handle(self, command: str) -> str:
        result = self.parser.parse(command)
        action = result.get("action")
        target = result.get("target")

        if action == "toggle_device":
            return self.ha_client.toggle_device(target)
        elif action == "move_temi":
            return self.ha_client.move_temi(target)
        else:
            return "Sorry, I didn't understand that instruction."
