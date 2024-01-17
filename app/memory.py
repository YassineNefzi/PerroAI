from langchain.schema import BaseMemory

from typing import Any, Dict, List

class ChatMemory(BaseMemory):
    history: List[str] = []
    memory_key: str = "history"
    memory_window: int = 4

    def clear(self):
        self.history.clear()

    @property
    def memory_variables(self) -> List[str]:
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        return {self.memory_key: "\n".join(self.history[-self.memory_window :])}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        formatted_input = f"<s>[INST] {inputs['input']} [/INST]"
        formatted_output = f"{outputs['response']}</s>"
        self.history.append(formatted_input)
        self.history.append(formatted_output)