import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from movie_API import movies

# Create FastAPI application
app = FastAPI()

# Create the first endpoint
@app.get("/")
async def root(min_popularity: int = 7):
    # Call the movies function with the specified min_popularity filter
    filtered_movies = movies(min_popularity=min_popularity)

    # Filter movies based on min_popularity
    filtered_movies = [movie for movie in filtered_movies if movie.get('popularity', 0) >= min_popularity]

    # Return the filtered movies as a JSON response
    return JSONResponse(content=filtered_movies)

#exemple filter
#http://127.0.0.1:8000/?min_popularity=800