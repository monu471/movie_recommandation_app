import streamlit as st
import pickle
import pandas as pd
import requests
similarity = pickle.load(open("similarity.pkl","rb"))
movie_dict = pickle.load(open("moviedict.pkl","rb"))
df = pd.DataFrame(movie_dict)
def fetch_poster(movie_id):
    responce = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=98b07d7f8bdba30671b2ccb19dd592f3".format(movie_id))
    data = responce.json()
    return "https://image.tmdb.org/t/p/original"+data["poster_path"]
def recommend(movie):
    movie_index = df[df["title"]==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies = []
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = df.iloc[i[0]].movie_id
        recommend_movies.append(df.iloc[i[0]].title)
        #fetch poster by api
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster
st.title("Movie Recommended System")
select_movie_name = st.selectbox(
    'How would you like to be contacted?',df["title"].values)
if st.button('Recommend'):
    name,poster = recommend(select_movie_name)
    ##layout of the page
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])

