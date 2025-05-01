import streamlit as st
from config import MANAGER_USERNAME, MANAGER_PASSWORD
from .create import create_tab
from .delete import delete_tab


def run():
    if not st.session_state.get("authenticated", False):
        show_login()
    else:
        show_dashboard()


def show_login():
    st.subheader("🔐 Manager Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == MANAGER_USERNAME and password == MANAGER_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials")


def show_dashboard():
    tab = st.radio("Choose Action", ["Create Movie", "Delete Movie"], horizontal=True)

    if tab == "Create Movie":
        create_tab()
    elif tab == "Delete Movie":
        delete_tab()
