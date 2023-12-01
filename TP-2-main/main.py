# main.py
import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from movie_API import movies

# Create FastAPI application
app = FastAPI()

# Create the first endpoint
@app.get("/")
async def root(movie_genre: int = None):
    # Call the movies function with the specified genre filter
    filtered_movies = movies(movie_genre=movie_genre)

    # Return the filtered movies as a JSON response
    return JSONResponse(content=filtered_movies)
