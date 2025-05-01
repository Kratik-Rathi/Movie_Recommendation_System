import pandas as pd
from db_utils import connect_to_db


def fetch_movies(title=None, year=None, language=None, country=None, director=None, genre=None, min_rating=None, max_rating=None):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.callproc('get_filtered_movies', (title, year, language, country, director, genre, min_rating, max_rating))
    rows = cur.fetchall()
    cols = ['ID', 'Title', 'Year', 'Language', 'Country', 'Director', 'Genres', 'Cast', 'Imdb_Rating', 'Content_Rating', 'Profit']
    df = pd.DataFrame(rows, columns=cols)
    cur.close(); conn.close()
    return df
