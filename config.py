import os
import streamlit as st

# Detect if we're on Streamlit Cloud
on_cloud = "STREAMLIT_ENVIRONMENT" in os.environ or "STREAMLIT_RUNTIME" in os.environ

if not on_cloud:
    from dotenv import load_dotenv
    load_dotenv()


def get_secret(key):
    return st.secrets[key] if on_cloud else os.getenv(key)


# Database
DB_NAME = get_secret("DB_NAME")
DB_USER = get_secret("DB_USER")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_HOST = get_secret("DB_HOST")
DB_PORT = get_secret("DB_PORT")

# Manager login
MANAGER_USERNAME = get_secret("MANAGER_USERNAME")
MANAGER_PASSWORD = get_secret("MANAGER_PASSWORD")
