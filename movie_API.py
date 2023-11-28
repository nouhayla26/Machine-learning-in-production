import requests
import random

# Define API key and base URL
api_key = "9cbc4d8610399f5e4c023fe8a815716c"
base_url = 'https://api.themoviedb.org/3/movie/popular'

# Function to get movies based on popularity
def movies(min_popularity=7):
    # Print the received min_popularity value for debugging
    print(f"movies function received min_popularity: {min_popularity}")

    # Set up request parameters
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }

    # Add popularity filter
    params['vote_average.gte'] = min_popularity

    # Make the API request
    response = requests.get(base_url, params=params)

    # Remove the popularity filter after the request
    del params['vote_average.gte']

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract movie data from the response
        data = response.json()
        movies_list = data.get('results', [])

        return movies_list[:100]

    else:
        # Return an error message if the request failed
        return {"error": f"API request error: {response.status_code}", "details": response.text}
