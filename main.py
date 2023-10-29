import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open("moviedict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))


st.markdown("""
This is a movie recommender system that uses machine learning to recommend movies to you based on your past preferences. To use the system, simply select a movie from the dropdown menu and click the "Show Recommendations" button.
""")


def recommend(movie):
    # if movie not in similarity:
    #     st.error('Movie has not been rated.')
    #     return []

    index = movies[movies['title']==movie].index[0]
    distance = similarity[index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    st.write('Recommended movies:')
    st.write(recommended_movies)
    return recommended_movies


st.header('Movie Recommender System')

movielist = movies['title'].values
selected_movie_name = st.selectbox(
    "Search your movie here",
    movielist
)

if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie_name)
    st.write(recommendations)

