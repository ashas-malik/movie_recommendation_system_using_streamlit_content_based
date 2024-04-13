# import streamlit as st
# import pickle
# import pandas as pd
#                                      # for fetching or using APIs
# import requests
#
# # the pandas library is unable to load the dataframe using pickle so instead of importing the dataframe we
# # will import it as a dictionary
#
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d24d96ab7dd3c7710fb503360997e455&language=en-US'.format(movie_id))
#
#     data = response.json()  # store response as json
#     return " https://image.tmdb.org/t/p/w500/ " + data['poster_path']
#
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]  # Now we need to sort the distances
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies_names = []
#     recommended_movies_posters = []
#     # now for adding movie posters to our web app we would use the movie_id
#
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movies_names.append(movies.iloc[i[0]].title)
#         # fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#
#     return recommended_movies_names , recommended_movies_posters
#
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # rb means read binary mode
# movies = pd.DataFrame(movies_dict)  # Make a dataframe with the title movies
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommender System')
#
# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies['title'].values)
# # st.write('You selected:', option)
#
# # Now add a button
# if st.button('Recommend'):
#     recommended_movies_names,recommended_movies_posters = recommend(selected_movie_name)      # make a function with the name recommend
#
#     # for i in recommendations:
#     #     st.write(i)
#
# col1, col2, col3, col4, col5 = st.columns(5)
#
# # with col1:
# #    st.header(names[0])
# #    st.image(posters[0])
#                             # instead of header use st.text for smaller font
# with col1:
#    st.text(recommended_movies_names[0])
#    st.image(recommended_movies_posters[0])
#
# with col2:
#    st.text(recommended_movies_names[1])
#    st.image(recommended_movies_posters[1])
#
# with col3:
#    st.text(recommended_movies_names[2])
#    st.image(recommended_movies_posters[2])
#
# with col4:
#    st.text(recommended_movies_names[3])
#    st.image(recommended_movies_posters[3])
#
# with col5:
#    st.text(recommended_movies_names[4])
#    st.image(recommended_movies_posters[4])

#8265bd1679663a7ea12ac168da84d2e8

import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=d24d96ab7dd3c7710fb503360997e455&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





