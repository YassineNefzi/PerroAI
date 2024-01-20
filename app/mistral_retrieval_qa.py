from langchain_community.llms.ollama import Ollama
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from .chat_wrapper import Mistral

system_template = """Use the following pieces of context to answer the user's question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
{context}"""

messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]

CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def retrieve_from_pdf(query: str):
    """Retrieves information from a PDF document based on a given query."""

    llm = Ollama(model="mistral-m3allem")
    model = Mistral(llm=llm, callbacks=[StreamingStdOutCallbackHandler()])
    loader = DirectoryLoader("./data/")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=0,
        length_function=len,
        is_separator_regex=False,
    )
    documents = loader.load()
    texts = text_splitter.split_documents(documents)
    db = Chroma.from_documents(embedding=HuggingFaceEmbeddings(), documents=texts)
    retriever = db.as_retriever()
    

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | CHAT_PROMPT
        | model
        | StrOutputParser()
    )
    answer = rag_chain.invoke(query)
    return answer
