from langchain_community.llms.ollama import Ollama
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

from .chat_wrapper import Samantha, Mistral


if __name__ == "__main__":
    llm = Ollama(model="mistral-m3allem")
    model = Mistral(llm=llm, callbacks=[StreamingStdOutCallbackHandler()])  # type: ignore
    loader = PyPDFLoader(file_path="./data/2310.05421.pdf")
    documents = loader.load()
    db = Chroma.from_documents(embedding=HuggingFaceEmbeddings(), documents=documents)
    retriever = db.as_retriever()
    chain = RetrievalQA.from_llm(llm=model, retriever=retriever, verbose=True)
    user_question = input("Ask a question: ")
    print(chain.invoke({"query": user_question}))
