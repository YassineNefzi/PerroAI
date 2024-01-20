from langchain_community.llms.ollama import Ollama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import ConversationChain
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.memory import ConversationBufferMemory

from .chat_wrapper import Samantha, Mistral
from .mistral_retrieval_qa import retrieve_from_pdf


class Chatbot:
    def __init__(self):
        self.llm = Ollama(model="mistral-m3allem")
        self.model = Mistral(llm=self.llm, callbacks=[StreamingStdOutCallbackHandler()])
        self.memory = ConversationBufferMemory(return_messages=True)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a chatbot designed to help children who have speech difficulties. \
             These children have trouble pronouncing certain sounds, and you are here to help them. \
             The child will say a word or a sentence which will translate to phonemes, and you will correct them if \
             they make a mistake and help them pronounce the word correctly if they need help. \
             Be playful with the child and encourage him or her to do better if they make a mistake \
             and praise them if they do well.",
                ),
                MessagesPlaceholder("history"),
                ("human", "{input}"),
            ]
        )
        self.chat_chain = ConversationChain(
            llm=self.model, prompt=self.prompt, memory=self.memory, verbose=True
        )

    def generate_response(self, user_input):
        """Generates a response based on the user input and context from various sources."""

        data = {"input": user_input}
        return self.chat_chain.invoke(data)
