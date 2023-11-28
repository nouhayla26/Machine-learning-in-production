import random
from fastapi import FastAPI
from create_API import movies
# Création de l'application fastAPI
app = FastAPI()
movies_titles = movies()

# Créer le premier edpoint
@app.get("/")
async def root():
    return movies_titles

