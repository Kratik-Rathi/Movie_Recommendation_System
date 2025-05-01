import streamlit as st
from db_utils import connect_to_db


def delete_tab():
    st.subheader("🗑️ Delete Movie")

    delete_by = st.radio("Delete By", ["Movie ID", "Title"], horizontal=True)
    movie_id, title = None, None

    if delete_by == "Movie ID":
        movie_id = st.number_input("Enter Movie ID", min_value=1)
    else:
        title = st.text_input("Enter Movie Title")

    if st.button("Delete Movie"):
        conn = connect_to_db()
        cur = conn.cursor()
        try:
            if movie_id:
                cur.execute("SELECT title FROM movies WHERE movie_id = %s", (movie_id,))
                result = cur.fetchone()
                if not result:
                    st.warning("No movie found with that ID.")
                    return
                cur.execute("DELETE FROM movies WHERE movie_id = %s", (movie_id,))
                st.success(f"✅ Deleted Movie ID {movie_id} – '{result[0]}'")
            elif title:
                cur.execute("SELECT movie_id FROM movies WHERE title = %s", (title,))
                result = cur.fetchone()
                if not result:
                    st.warning("No movie found with that title.")
                    return
                cur.execute("DELETE FROM movies WHERE title = %s", (title,))
                st.success(f"✅ Deleted '{title}' (ID: {result[0]})")
            conn.commit()
        except Exception as e:
            conn.rollback()
            st.error(f"❌ Error deleting: {e}")
        finally:
            cur.close(); conn.close()
