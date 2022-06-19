import pandas as pd
import numpy as np
from flask import Flask, request
import math
from .movie_fetcher import session

from .models import model_deps, user, movies 

app = Flask(__name__)
model_deps.start_mappers()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        request_body = request.json
        uid = request_body['uid']
        if 'rating' in list(request_body.keys()):
            rating = request_body['rating']
        else:
            rating = False
        movies = pd.read_csv('/src/movies/entrypoints/movie_results.csv')
        users = pd.read_csv('/src/movies/entrypoints/users.csv') 
        if uid < 0 or uid > users.shape[0] - 1:
            return {
                'message': 'invalid user id'
            }, 401
        elif type(rating) != bool:
            return {
                'message': 'rating must be a boolean value'
            }, 401
        else:
            pref_key = users.iloc[int(uid)].preference_key
            if rating:
                # Ascending order
                recommended_movies = movies[movies.preference_key == pref_key].sort_values('rating').movie_title
            else:
                # Descending order
                recommended_movies = movies[movies.preference_key == pref_key].sort_values('rating', ascending=False).movie_title

            return {
                'recommended_movies': list(recommended_movies)
            }, 200
    except:
        return {
            'message': 'server error'
        }, 500

@app.route("/login", methods=["POST"])
def login():
    try:
        request_body = request.json
        email = request_body['email']
        password = request_body['password']
        users = pd.read_csv('/src/movies/entrypoints/users.csv')
        if str(email) not in list(users.email):
            return {
                'message': 'this account does not exist'
            }, 401
        else:
            if str(password) != users[(users.email == str(email))].iloc[0].password:
                return {
                    'message': 'wrong email or password'
                }, 401
            else:
                uid = users[(users.email == str(email))].iloc[0]['Unnamed: 0']
                return {
                    'message': 'auth',
                    'uid': str(uid)
                }, 200
    except:
        return {
            'message': 'server error'
        }, 500

@app.route("/signup", methods=["POST"])
def signup():
    try:
        request_body = request.json
        email = request_body['email']
        password = request_body['password']
        preferences = request_body['preferences']
        genres = preferences.split(',')
        key = [1 if genre == 'Comedy' 
            else 2 if genre == 'Drama' 
            else 3 if genre == 'Sci-Fi'
            else 4 if genre == 'Romantic'
            else 5 if genre == 'Adventure' else 0 for genre in genres]
        preference_key = math.prod(key) % 5 + 1
        users = pd.read_csv('/src/movies/entrypoints/users.csv')
        if str(email) not in list(users.email):
            new_user = pd.DataFrame({
                'email': [email],
                'password': [password],
                'preferences': [preferences],
                'preference_key': [preference_key]
            }, index=[users.email.size])
            new_user.to_csv('/src/movies/entrypoints/users.csv', mode='a', index=users.email.size, header=False)
            return {
                'message': 'user succesfully registered'
            }, 200
        else:
            return {
                'message': 'User already exists'
            }, 409
    except:
        return {
            'message': 'server error'
        }, 500