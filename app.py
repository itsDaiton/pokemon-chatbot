import streamlit as st
from services.auth import *
from ui.chat_ui import render_chat
from ui.login_ui import render_login_screen
from services.preprocessing import *
from services.embedding import *

st.set_page_config(page_title="Pokémon Chatbot", layout="wide")


def login_screen():
    render_login_screen()


def main_app(user):
    # if st.button("Logout"):
    #   logout()
    render_chat()


user = get_user()

if user and is_admin(user):
    main_app(user)
else:
    login_screen()


with st.sidebar:
    st.title("🐱‍👓Pokémon Chatbot")

    if "vectorstore" not in st.session_state:
        with st.spinner("Creating vectorstore..."):
            docs = load_data("data/poke_corpus.csv")
            docs_split = split_documents(docs=docs, chunk_size=1000, chunk_overlap=150)
            embedding_model = get_embedding_model()
            vectorsore = get_vectorstore(
                embedding_model=embedding_model, docs=docs_split
            )
            st.session_state["vectorstore"] = vectorsore
            st.success("Vectorstore created successfully!")
    else:
        vectorsore = st.session_state["vectorstore"]
