import uvicorn
from fastapi import FastAPI # import de la classe FastAPI
app = FastAPI() # Création de l application
@app.get("/") # Traitement de la requête get http
def hello() -> str: # Valeur de retour pour la réponse http
    return "Hello World"
if __name__ == "__main__":
    uvicorn.run(app) # lancement du serveur HTTP + WSGI avec les options de debug

