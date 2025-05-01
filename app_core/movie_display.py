import streamlit.components.v1 as components


def render_movie_cards(df):
    html = """
    <style>
    .movie-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        justify-content: flex-start;
        padding: 20px 0;
        position: relative;
        overflow: visible;
    }
    .movie-card {
        background-color: #222;
        color: white;
        width: 200px;
        height: 120px;
        border-radius: 10px;
        padding: 10px;
        box-sizing: border-box;
        text-align: center;
        position: relative;
        transition: transform 0.2s ease;
        overflow: visible;
        z-index: 1;
    }
    .movie-card:hover {
        transform: scale(1.05);
        z-index: 999;
    }
    .movie-tooltip {
        display: none;
        position: absolute;
        top: 0;
        left: 100%;
        margin-left: 10px;
        width: 240px;
        background-color: #333;
        color: white;
        padding: 10px;
        border-radius: 8px;
        z-index: 9999;
        font-size: 13px;
        text-align: left;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        white-space: normal;
        word-wrap: break-word;
        pointer-events: none;
    }
    .movie-card:hover .movie-tooltip {
        display: block;
    }
    .movie-card:nth-child(5n) .movie-tooltip {
        left: auto;
        right: 100%;
        margin-left: 0;
        margin-right: 10px;
    }
    </style>
    <div class="movie-grid">
    """

    for _, row in df.iterrows():
        html += f"""
        <div class="movie-card">
            <strong>{row['Title']}</strong><br>
            <span style="color:#bbb;">{row['Year']}</span>
            <div class="movie-tooltip">
                <b>Director:</b> {row['Director']}<br>
                <b>Genres:</b> {row['Genres']}<br>
                <b>Cast:</b> {row['Cast']}<br>
                <b>Language:</b> {row['Language']}<br>
                <b>Country:</b> {row['Country']}<br>
                <b>IMDb Rating:</b> {row['Imdb_Rating']}<br>
                <b>Content Rating:</b> {row['Content_Rating']}<br>
                <b>Profit:</b> ${row['Profit']:,.2f}
            </div>
        </div>
        """
    html += "</div>"
    estimated_height = ((len(df) - 1) // 5 + 1) * 160 + 50
    components.html(html, height=estimated_height, scrolling=False)
