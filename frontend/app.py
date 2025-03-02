import streamlit as st
import requests

st.title("📚 AI Documentation Chatbot")

query = st.text_input("Ask a question:")

if st.button("Submit") and query:
    with st.spinner("Searching..."):
        response = requests.get(f"http://127.0.0.1:8000/ask/?query={query}")
        answer = response.json()["response"]
    
    st.markdown(f"**Answer:** {answer}")
