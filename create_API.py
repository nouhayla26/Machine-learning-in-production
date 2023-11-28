import random
from fastapi import FastAPI

# Création de l'application fastAPI
app = FastAPI()


# Créer le premier edpoint
@app.get("/")
async def root():
    return {"Messsage" : "Bienvenue sur notre API de génération de nombre aléatoires"}

