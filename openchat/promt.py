from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.header("research ai")

user_input = st.text_input("Enter your prompt")

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.7)
def generate_response(prompt: str) -> str:
    message = llm.invoke(prompt)
    if isinstance(message.content, list):
        return "".join(part.get("text", "") for part in message.content)
    return message.content or ""

if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("Thinking..."):
            try:
                st.write(generate_response(user_input))
            except Exception as exc:
                st.error(f"Request failed: {exc}")