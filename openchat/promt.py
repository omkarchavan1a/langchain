from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.markdown(
    """
    <style>
        .main-header {
            font-size: 2.8rem;
            text-align: center;
            letter-spacing: 2px;
            color: #22223b;
            margin-bottom: 16px;
            font-family: 'Segoe UI', 'Roboto', sans-serif;
        }
        .stTextInput > label, .stSelectbox > label {
            color: black !important;
            font-weight: 500 !important;
            font-size: 1.13rem !important;
        }
        .stSelectbox, .stTextInput {
            padding: 12px;
            border-radius: 10px;
        }
        .stApp {
            background: linear-gradient(120deg, #d1d9e6 40%, #b8c0ff 100%);
            color: black !important;
        }  
        .stButton{
            color:white
        }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="main-header">AI Research Paper Generator</div>', unsafe_allow_html=True)

paper_input = st.text_input("📄 Enter research paper name", placeholder="e.g. Quantum Computing Applications", key="paper_input")

style_input = st.selectbox(
    "🎨 Select a style",
    ["Academic", "Technical", "Creative", "Persuasive", "Narrative"],
    index=0,
    key="style_input",
)

length_input = st.selectbox(
    "✍️ Select length",
    ["Short", "Medium", "Long"],
    index=1,
    key="length_input",
)


#template
template = PromptTemplate(
    template = """
Research Paper Type: {paper_input}
Writing Style: {style_input}
Desired Length: {length_input}

Title: [Enter your research paper title here]

Abstract:
[Provide a concise summary of the research paper, outlining the key problem, approach, and findings.]

Introduction:
[Introduce the background and importance of the topic, clearly state the research question or objective.]

Literature Review / Background:
[Summarize key existing research and theories relevant to your topic. Relate past findings to your current work.]

Methodology:
[Describe the methods used for investigation, data collection, or experimentation. Explain why these methods are appropriate.]

Results / Findings:
[Present the significant results or findings of your research. Use charts, tables, or figures as needed.]

Discussion:
[Interpret and discuss the implications of your findings. Highlight limitations, challenges, or interesting patterns.]

Conclusion:
[Summarize the main points of the paper and suggest future research directions or practical applications.]

References:
[List the references, articles, or books cited in your paper in the appropriate format.]

Appendices (if applicable):
[Provide any supplementary materials, such as raw data, questionnaires, or additional images.]
 """
)

input_variables = ["paper_input", "style_input", "length_input"]

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input
})

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.7)

def generate_response(prompt: str) -> str:
    message = llm.invoke(prompt)
    if isinstance(message.content, list):
        return "".join(part.get("text", "") for part in message.content)
    return message.content or ""

if st.button("Generate"):
    # Convert prompt to string before calling strip(), since it's a StringPromptValue object
    prompt_str = str(prompt)
    if not prompt_str.strip():
        st.warning("Please select a paper type, style, and length first.")
    else:
        with st.spinner("Thinking..."):
            try:
                st.write(generate_response(prompt_str))
            except Exception as exc:
                st.error(f"Request failed: {exc}")