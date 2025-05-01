import streamlit as st


def get_secret(key):
    return st.secrets[key]


# Database
DB_NAME = get_secret("DB_NAME")
DB_USER = get_secret("DB_USER")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_HOST = get_secret("DB_HOST")
DB_PORT = get_secret("DB_PORT")

# Manager login
MANAGER_USERNAME = get_secret("MANAGER_USERNAME")
MANAGER_PASSWORD = get_secret("MANAGER_PASSWORD")
