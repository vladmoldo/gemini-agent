import os
from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = FastAPI()

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Create a conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory()
)

@app.post("/chat")
async def chat(message: str):
    response = conversation.predict(input=message)
    return {"response": response}

@app.get("/")
async def root():
    return {"message": "Gemini Chat Agent is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
