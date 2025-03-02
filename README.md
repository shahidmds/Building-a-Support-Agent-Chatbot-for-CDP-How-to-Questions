Building a Support Agent Chatbot for CDP

📌 Objective

Develop a chatbot that can answer "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from their official documentation to guide users.

🔗 Data Sources

Segment Documentation

mParticle Documentation

Lytics Documentation

Zeotap Documentation

⚡ Features

Natural Language Processing (NLP): Understands and processes user queries.

Documentation Retrieval: Fetches relevant information from CDP documentation.

Vector Search: Uses FAISS for semantic search.

AI-Powered Responses: Utilizes Google Gemini API.

Handles Question Variations: Supports different phrasings and prevents irrelevant queries.

Cross-CDP Comparisons: Answers questions about differences between CDPs.

Advanced "How-to" Queries: Provides guidance on complex configurations and integrations.

🛠 Tech Stack

Backend: FastAPI, Python

AI & NLP: Google Gemini-2.0 API, FAISS, Sentence Transformers

Data Storage: JSON (for document storage), FAISS index for embeddings

Web Scraping (Optional): BeautifulSoup/Selenium

Deployment: AWS/GCP, Uvicorn
