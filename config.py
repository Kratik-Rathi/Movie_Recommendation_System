import os
import streamlit as st

# Try loading from .env only if not running on Streamlit Cloud
if not st.secrets:
    from dotenv import load_dotenv
    load_dotenv()

# Fallback logic — local: os.getenv, Cloud: st.secrets
def get_secret(key):
    return st.secrets.get(key) or os.getenv(key)

# Database credentials
DB_NAME = get_secret("DB_NAME")
DB_USER = get_secret("DB_USER")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_HOST = get_secret("DB_HOST")
DB_PORT = get_secret("DB_PORT")

# Manager login
MANAGER_USERNAME = get_secret("MANAGER_USERNAME")
MANAGER_PASSWORD = get_secret("MANAGER_PASSWORD")
