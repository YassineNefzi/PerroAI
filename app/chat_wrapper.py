from langchain_community.llms.ollama import Ollama
from langchain_experimental.chat_models.llm_wrapper import ChatWrapper

class CustomChatWrapper(ChatWrapper):
    llm: Ollama


class Llama2Chat(CustomChatWrapper):
    @property
    def _llm_type(self) -> str:
        return "llama-2-chat"

    sys_beg: str = "<s>[INST] <<SYS>>\n"
    sys_end: str = "\n<</SYS>>\n\n"
    ai_n_beg: str = " "
    ai_n_end: str = " </s>"
    usr_n_beg: str = "<s>[INST] "
    usr_n_end: str = " [/INST]"
    usr_0_beg: str = ""
    usr_0_end: str = " [/INST]"

class Samantha(CustomChatWrapper):
    @property
    def _llm_type(self) -> str:
        return "llama-2-chat"

    sys_beg: str = "<|im_start|>system\n"
    sys_end: str = "<|im_end|>"
    ai_n_beg: str = ""
    ai_n_end: str = "<|im_end|>"
    usr_n_beg: str = "\n<|im_start|>user\n"
    usr_n_end: str = "<|im_end|>\n<|im_start|>assistant\n"