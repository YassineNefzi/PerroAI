from fastapi import FastAPI, HTTPException, status

from app.chatbot import Chatbot
from app.mistral_retrieval_qa import retrieve_from_pdf
import uvicorn

app = FastAPI()

chatbot = Chatbot()


@app.post("/talk")
def talk(input: str):
    response = chatbot.generate_response(input)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No response found"
        )
    return {"response": response}


@app.post("/retrieve_from_pdf")
def retrieve(query: str):
    answer = retrieve_from_pdf(query)
    if answer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No answer found"
        )
    return {"answer": answer}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)