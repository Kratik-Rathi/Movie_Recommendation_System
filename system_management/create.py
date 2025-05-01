import streamlit as st
from db_utils import connect_to_db


@st.cache_data
def get_dropdown_data():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT country FROM movies ORDER BY country")
    countries = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT DISTINCT content_rating FROM movies ORDER BY content_rating")
    ratings = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT DISTINCT language FROM movies ORDER BY language")
    languages = [row[0] for row in cur.fetchall()]
    cur.execute("SELECT genre_id, genre FROM genres ORDER BY genre")
    genres = cur.fetchall()
    cur.close(); conn.close()
    return countries, ratings, {g[1]: g[0] for g in genres}, languages


def fix_movie_id_sequence():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT setval('movies_movie_id_seq', (SELECT MAX(movie_id) FROM movies) + 1);")
    conn.commit()
    cur.close(); conn.close()


def create_tab():
    st.subheader("🎬 Add New Movie")

    if st.button("🔄 Fix ID Sequence"):
        fix_movie_id_sequence()
        st.success("✅ Sequence reset to MAX(movie_id) + 1.")

    countries, ratings, genre_dict, languages = get_dropdown_data()

    title = st.text_input("Title")
    year = st.number_input("Year", min_value=1900, max_value=2100)
    duration = st.number_input("Duration (minutes)", min_value=1)
    language = st.selectbox("Language", languages)
    country = st.selectbox("Country", countries)
    rating = st.selectbox("Content Rating", ratings)
    imdb = st.number_input("IMDb Rating", 0.0, 10.0, step=0.1)
    budget = st.number_input("Budget (USD)", min_value=0.0)
    gross = st.number_input("Gross (USD)", min_value=0.0)
    profit = gross - budget
    genres = st.multiselect("Genres", list(genre_dict.keys()))
    director = st.text_input("Director Name")
    actor1 = st.text_input("Actor 1 (required)")
    actor2 = st.text_input("Actor 2 (optional)")
    actor3 = st.text_input("Actor 3 (optional)")

    if st.button("Submit Movie"):
        if not title or not actor1 or not genres:
            st.error("Please fill required fields.")
            return

        conn = connect_to_db()
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO movies (title, year, duration, language, country, content_rating, imdb_score, budget, gross, profit, director_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING movie_id
            """, (title, year, duration, language, country, rating, imdb, budget, gross, profit, director))
            movie_id = cur.fetchone()[0]

            cur.execute("INSERT INTO casts (movie_id, title, actor_1, actor_2, actor_3) VALUES (%s, %s, %s, %s, %s)",
                        (movie_id, title, actor1, actor2, actor3))

            for g in genres:
                cur.execute("INSERT INTO movie_genres_mapping (movie_id, title, genre_id) VALUES (%s, %s, %s)",
                            (movie_id, title, genre_dict[g]))

            conn.commit()
            st.success(f"✅ Movie '{title}' created (ID: {movie_id})")
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Failed to insert: {e}")
        finally:
            cur.close(); conn.close()
