import pandas as pd
import numpy as np
import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from things import similarity

data = pd.read_csv("names.csv")

#things


def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_images = []
    for i in movies_list:
        recommended_movies.append(data.iloc[i[0]].title)
    return recommended_movies



movie = data['title'].tolist()
selected_movie = st.selectbox('Select a movie' , movie)
 
import streamlit.components.v1 as components

if st.button("🎬 Recommend"):
    recommended_movies = recommend(selected_movie)

    html_code = """
    <style>
    body {
        margin: 0;
    }

    .movie-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 25px;
        padding: 20px;
    }

    .movie-card {
        background: linear-gradient(145deg, #1e1e1e, #2c2c2c);
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        color: white;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        transition: 0.3s ease;
        white-space: normal;
        word-break: keep-all;
    }

    .movie-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.6);
    }

    .fade-in {
        animation: fadeUp 0.6s ease forwards;
        opacity: 0;
    }

    @keyframes fadeUp {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>

    <div class="movie-grid">
    """

    for movie in recommended_movies:
        html_code += f"""
        <div class="movie-card fade-in">
            🎬 {movie}
        </div>
        """

    html_code += "</div>"

    components.html(html_code, height=600, scrolling=True)