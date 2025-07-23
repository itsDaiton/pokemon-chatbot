import streamlit as st


def login(email, password):
    if email == st.secrets["ADMIN_EMAIL"] and password == st.secrets["ADMIN_PASSWORD"]:
        st.session_state["user"] = {"email": email}
        return True
    else:
        return False


def logout():
    st.session_state.pop("user", None)


def get_user():
    return st.session_state.get("user", None)


def is_admin(user):
    return user is not None and user.get("email") == st.secrets["ADMIN_EMAIL"]
