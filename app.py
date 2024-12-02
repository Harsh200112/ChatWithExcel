import os
import warnings
import nest_asyncio
import streamlit as st
from DataLoading.Data import get_data
from llama_index.core import Settings
from llama_index.llms.groq import Groq
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import StorageContext, load_index_from_storage

nest_asyncio.apply()
warnings.filterwarnings("ignore")

def init_llm(model_name):
    return Groq(model=model_name, api_key=os.environ.get("GROQ_API_KEY"))

@st.cache_resource
def load_index(selected_model):
    curr_direc = os.getcwd()
    file_path = os.path.join(curr_direc, 'processed_data.csv')
    # print(file_path)
    get_data(file_path)
    model = init_llm(selected_model)
    embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

    Settings.embed_model = embedding_model
    Settings.llm = model

    vector_store = FaissVectorStore.from_persist_dir('storage')
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store, persist_dir='storage'
    )
    index = load_index_from_storage(storage_context=storage_context)
    return index.as_query_engine()

st.title("Chatbot from ClienterAI")

st.sidebar.header("Settings")
selected_model = st.sidebar.selectbox(
    "Select Groq Model:",
    options=["mixtral-8x7b-32768", "gemma2-9b-it", "llama-3.1-70b-versatile", "llama3-8b-8192", "llava-v1.5-7b-4096-preview"],
    index=0
)

query_engine = load_index(selected_model)

if "messages" not in st.session_state:
    st.session_state["messages"] = []


with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask a question based on your data:", "")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    response = query_engine.query(user_input)
    ai_response = response
    st.session_state["messages"].append({"role": "assistant", "content": ai_response})

for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Assistant:** {message['content']}")

if st.sidebar.button("Clear Chat"):
    st.session_state["messages"] = []
    st.sidebar.success("Chat cleared!")


st.markdown("""
    <style>
            .stForm {
            position: fixed;
            align-self: center;
            bottom: 0;
            width: 50%;
            left: 25%;
            right: 50%;
            padding: 10px;
        }
    <style>
""", unsafe_allow_html=True)