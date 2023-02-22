from fastapi import FastAPI
from pydantic import BaseModel #Modelode de Clase
from typing import List #Libreria para Lis
from uuid import uuid4 #Para generar los id's de forma aleatoria

#CRUD
app = FastAPI()

@app.get("/") 
async def hola():
    return {"message": "Hola mundo"}
#Almacenamos en la lista, para no almacenar en base de datos
estud = []

class Estudiante(BaseModel):
    id : str
    nom : str
    apell : str
    edad : int
    habi : List [str] = []

    
@app.get("/studs")
async def studs():
    return estud

@app.post("/studes")
async def add_stud(stud:Estudiante):
    estud.id = str(uuid4()) #Pedimos que antes nos genere un id de forma string
    estud.append(stud.dict())#Convertimos a diccionario la información que se agrega en la lista
    return "Estudiante agregado con exito" #Retornamos un mensaje
    