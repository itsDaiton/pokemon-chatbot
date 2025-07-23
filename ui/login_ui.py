import streamlit as st
from services.auth import *


def render_login_screen():
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.title("🔐 Pokébot Authentication")
        st.markdown("Please enter the specified credentials to access the chatbot.")
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form", border=True):
            email = st.text_input("Email", placeholder="you@example.com")
            password = st.text_input(
                "Password", type="password", placeholder="••••••••"
            )

            submit = st.form_submit_button("Login", type="primary")

            if submit:
                success = login(email, password)
                if not success:
                    st.error("Invilid email or password.")
