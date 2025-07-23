import streamlit as st
from services.chat import *
from services.embedding import *
from langchain_core.runnables import RunnablePassthrough


def render_chat():
    st.title("💬 Pokémon Chat")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Say something to Pikachu..."):
        st.session_state["messages"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        retriever = get_retriever(st.session_state["vectorstore"])
        prompt_template = get_system_prompt()
        llm = get_llm()

        rag_chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough(),
            }
            | prompt_template
            | llm
        )

        with st.spinner("Thinking..."):
            response = rag_chain.invoke(prompt)
        answer = response.content

        with st.chat_message("assistant"):
            full_response = ""
            message_placeholder = st.empty()

            for chunk in rag_chain.stream(prompt):
                full_response += chunk.content or ""
                message_placeholder.markdown(full_response)

        message_placeholder.markdown(full_response)
        st.session_state["messages"].append({"role": "assistant", "content": answer})
