import streamlit as st
from app_core import get_filter_options, fetch_movies, render_movie_cards
from system_management import run as manager_run

st.set_page_config(page_title="🎥 Movie Recommender", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "main"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

col1, col2 = st.columns([10, 2])
with col2:
    if st.session_state.page == "main":
        if st.button("🔐 Manager Login"):
            st.session_state.page = "manager"
            st.rerun()
    elif st.session_state.page == "manager":
        if st.button("⬅️ Main Page"):
            st.session_state.page = "main"
            st.session_state.authenticated = False
            st.rerun()

if st.session_state.page == "main":
    st.title("🎬 Movie Recommendation System")
    years, languages, countries, directors, genres = get_filter_options()

    if "search_results" not in st.session_state:
        st.session_state["search_results"] = fetch_movies()

    view_mode = st.radio("View Mode:", ("Grid View", "Table View"), horizontal=True)
    search_title = st.text_input("🔍 Search by Movie Title")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        year = st.selectbox("Year", [None] + years)
    with col2:
        language = st.selectbox("Language", [None] + languages)
    with col3:
        country = st.selectbox("Country", [None] + countries)
    with col4:
        director = st.selectbox("Director", [None] + directors)
    with col5:
        genre = st.selectbox("Genre", [None] + genres)
    with col6:
        rating_range = st.selectbox("IMDb Rating", [
            "All Ratings", "0–3", "3–5", "5–7", "7–8.5", "8.5+"
        ])

    min_rating, max_rating = None, None
    if rating_range != "All Ratings":
        if rating_range == "0–3": min_rating, max_rating = 0.0, 3.0
        elif rating_range == "3–5": min_rating, max_rating = 3.0, 5.0
        elif rating_range == "5–7": min_rating, max_rating = 5.0, 7.0
        elif rating_range == "7–8.5": min_rating, max_rating = 7.0, 8.5
        elif rating_range == "8.5+": min_rating = 8.5

    if st.button("Search"):
        title = search_title.strip() if search_title.strip() else None
        df = fetch_movies(title, year, language, country, director, genre, min_rating, max_rating)
        if df.empty:
            st.warning("No movies found.")
        else:
            st.session_state["search_results"] = df

    df = st.session_state["search_results"]
    if view_mode == "Grid View":
        render_movie_cards(df)
    else:
        st.dataframe(df)

elif st.session_state.page == "manager":
    st.title("🎛️ Manager Dashboard")
    manager_run()
