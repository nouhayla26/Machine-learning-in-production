# create_api.py
from fastapi import FastAPI
from movie_api import movies

app = FastAPI()

movies_data = movies()  # Load the complete list of movies on application startup

@app.get("/")
async def root(movie_genre: int = None):
    filtered_movies = movies(movie_genre=movie_genre)

    return filtered_movies
