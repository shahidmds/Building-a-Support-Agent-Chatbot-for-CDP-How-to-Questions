from fastapi import FastAPI
from retriever import retrieve_docs
import google.generativeai as genai
import os

# Set up Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCsBjo6SKSbx-6bc2u7lSgm3_6M5jFH43s"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

app = FastAPI()

@app.get("/ask/")
async def ask_question(query: str):
    context = " ".join(retrieve_docs(query))
    prompt = f"Docs:\n{context}\n\nAnswer: {query}"
    response = gemini_model.generate_content(prompt)
    return {"response": response.text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
