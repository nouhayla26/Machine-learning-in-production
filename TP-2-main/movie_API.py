# movie_api.py
import requests

# Define API key and base URL
api_key = "9cbc4d8610399f5e4c023fe8a815716c"
base_url = 'https://api.themoviedb.org/3/discover/movie'

# Function to get movies based on genre
def movies(movie_genre=None):
    # Set up request parameters
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }

    # Add genre filter
    if movie_genre:
        params['with_genres'] = movie_genre

    # Make the API request
    response = requests.get(base_url, params=params)

    # Remove the genre filter after the request
    if 'with_genres' in params:
        del params['with_genres']

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract movie data from the response
        data = response.json()
        movies_list = data.get('results', [])

        return movies_list[:100]

    else:
        # Return an error message if the request failed
        return {"error": f"API request error: {response.status_code}", "details": response.text}
