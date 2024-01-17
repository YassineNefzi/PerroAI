from langchain_community.llms.ollama import Ollama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferMemory

from .chat_wrapper import Samantha

class Chatbot:
    
    def __init__(self):
        
        self.llm = Ollama(model='samantha')
        self.model = Samantha(llm=self.llm, callbacks=[StreamingStdOutCallbackHandler()])
        self.memory = ConversationBufferMemory(return_messages=True)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a chatbot designed to be a companion for children."),
            MessagesPlaceholder("history"),
            ("human", "{input}")
        ])
        self.chat_chain = ConversationChain(llm=self.model, prompt=self.prompt, memory=self.memory, verbose=True)

    def generate_response(self):
        while True:
            user_input = input("\nYou: ")
            input_data = {"input": user_input}
            if user_input == "quit":
                break
            print("AI: ")
            _ = self.chat_chain.invoke(input_data)
            