-- CREATE MOVIES TABLE
CREATE TABLE Movies (
    Movie_ID SERIAL PRIMARY KEY,
    Title TEXT NOT NULL,
    Year INT,
    Duration INT,
    Language TEXT,
    Country TEXT,
    Content_Rating TEXT,
    Imdb_Score REAL,
    Budget DOUBLE PRECISION,
    Gross DOUBLE PRECISION,
    Profit DOUBLE PRECISION,
    Director_Name TEXT
);

-- CREATE GENRES TABLE

CREATE TABLE Genres (
    Genre_ID SERIAL PRIMARY KEY,
    Genre TEXT UNIQUE NOT NULL
);

-- CREATE MOVIE-GENRE MAPPING TABLE

CREATE TABLE Movie_Genres_Mapping (
    Movie_ID INT NOT NULL,
    Genre_ID INT NOT NULL,
    Title TEXT,
    PRIMARY KEY (Movie_ID, Genre_ID),
    FOREIGN KEY (Movie_ID) REFERENCES Movies(Movie_ID) ON DELETE CASCADE,
    FOREIGN KEY (Genre_ID) REFERENCES Genres(Genre_ID) ON DELETE CASCADE
);

-- CREATE CASTS TABLE

CREATE TABLE Casts (
    Movie_ID INT NOT NULL,
    Title TEXT,
    Actor_1 TEXT,
    Actor_2 TEXT,
    Actor_3 TEXT,
    FOREIGN KEY (Movie_ID) REFERENCES Movies(Movie_ID) ON DELETE CASCADE
);


-- Stored Procedure/function for searching movies:
CREATE OR REPLACE FUNCTION get_filtered_movies(
    p_title TEXT,
    p_year INT,
    p_language TEXT,
    p_country TEXT,
    p_director TEXT,
    p_genre TEXT,
    p_min_rating FLOAT,
    p_max_rating FLOAT
)
RETURNS TABLE (
    id INT,
    title TEXT,
    year INT,
    language TEXT,
    country TEXT,
    director TEXT,
    genres TEXT,
    casts TEXT,
    imdb_rating FLOAT,
    content_rating TEXT,
    profit FLOAT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        m.movie_id,
        m.title,
        m.year,
        m.language,
        m.country,
        m.director_name,
        string_agg(g.genre, ', ') AS genres,
        CONCAT_WS(', ', c.actor_1, c.actor_2, c.actor_3) AS casts,
        m.imdb_score,
        m.content_rating,
        m.profit
    FROM movies m
    JOIN movie_genres_mapping mgm ON m.movie_id = mgm.movie_id
    JOIN genres g ON mgm.genre_id = g.genre_id
    JOIN casts c ON m.movie_id = c.movie_id
    WHERE (p_title IS NULL OR m.title ILIKE '%' || p_title || '%')
      AND (p_year IS NULL OR m.year = p_year)
      AND (p_language IS NULL OR m.language = p_language)
      AND (p_country IS NULL OR m.country = p_country)
      AND (p_director IS NULL OR m.director_name = p_director)
      AND (p_genre IS NULL OR g.genre = p_genre)
      AND (p_min_rating IS NULL OR m.imdb_score >= p_min_rating)
      AND (p_max_rating IS NULL OR m.imdb_score <= p_max_rating)
    GROUP BY m.movie_id, m.title, m.year, m.language, m.country, m.director_name, m.imdb_score, m.content_rating, m.profit,
             c.actor_1, c.actor_2, c.actor_3;
END;
$$ LANGUAGE plpgsql;

-- fixing or setting movie_id to max so that new movie gets added in sequence and to avoid errors
SELECT setval('movies_movie_id_seq', (SELECT MAX(movie_id) FROM movies) + 1);




