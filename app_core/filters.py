from db_utils import connect_to_db


def get_filter_options():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT year FROM movies ORDER BY year")
    years = [r[0] for r in cur.fetchall()]
    cur.execute("SELECT DISTINCT language FROM movies ORDER BY language")
    languages = [r[0] for r in cur.fetchall()]
    cur.execute("SELECT DISTINCT country FROM movies ORDER BY country")
    countries = [r[0] for r in cur.fetchall()]
    cur.execute("SELECT DISTINCT director_name FROM movies ORDER BY director_name")
    directors = [r[0] for r in cur.fetchall()]
    cur.execute("SELECT genre FROM genres")
    genres = [r[0] for r in cur.fetchall()]
    cur.close(); conn.close()
    return years, languages, countries, directors, genres
