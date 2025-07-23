import os
import streamlit as st
from langchain_voyageai import VoyageAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document


def get_embedding_model(model: str = "voyage-3.5-lite") -> VoyageAIEmbeddings:
    return VoyageAIEmbeddings(model=model, voyage_api_key=st.secrets["VOYAGE_API_KEY"])


def get_vectorstore(
    embedding_model: VoyageAIEmbeddings,
    docs: list[Document],
    persist_path: str = "vectorstore/voyage",
) -> Chroma:
    if os.path.exists(persist_path):
        return Chroma(
            persist_directory=persist_path, embedding_function=embedding_model
        )
    else:
        return Chroma.from_documents(
            documents=docs,
            embedding=embedding_model,
            persist_directory=persist_path,
        )


def get_retriever(vectorstore: Chroma, search_kwargs: dict = None):
    if search_kwargs is None:
        search_kwargs = {"k": 5}
    return vectorstore.as_retriever(search_kwargs=search_kwargs)
