import requests
import random

# Clé API TMDB (remplacez 'YOUR_API_KEY' par votre clé réelle)
api_key = "9cbc4d8610399f5e4c023fe8a815716c"

# URL de base de l'API TMDB pour la liste des films populaires
base_url = 'https://api.themoviedb.org/3/movie/popular'

# Paramètres de la requête
params = {
    'api_key': api_key,
    'language': 'en-US',
    'page': 1  # Vous pouvez ajuster la page si vous souhaitez obtenir plus de résultats
}

    
def movies(): 
    
    # Effectuer la requête API
    response = requests.get(base_url, params=params)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200 :
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire la liste des films depuis les données
        movies = data.get('results', [])

        # Sélectionner 100 films au hasard
        random_movies = random.sample(movies, min(100, len(movies)))

        return random_movies

    else:
        # Afficher un message d'erreur si la requête a échoué
        print(f"Erreur de requête API: {response.status_code}")
        print(response.text)
