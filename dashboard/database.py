import uvicorn
import sqlite3
con = sqlite3.connect("tutorial.db")
from fastapi import FastAPI # import de la classe FastAPI
app = FastAPI() # Création de l application
@app.get("/") # Traitement de la requête get http
