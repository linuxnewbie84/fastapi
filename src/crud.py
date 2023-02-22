from fastapi import FastAPI
from pydantic import BaseModel #Modelode de Clase
from typing import List #Libreria para Lis
from uuid import uuid4 #Para generar los id's de forma aleatoria

#CRUD
app = FastAPI()

#Damos la bienvenidad

@app.get("/") 
async def hola():
    return "Bienvenido al CRUD de los Estudiantes"

#Almacenamos en la lista, para no almacenar en base de datos

estud = []

#Clase de los datos del Estudiante

class Estudiante(BaseModel):
    id : str
    nom : str
    apell : str
    edad : int
    habi : List [str] = []

#Metódo GET para visualizar la lista de estudiantes
    
@app.get("/studs")
async def studs():
    return estud

#Agregar Estudiante a la Lista

@app.post("/studes")
async def add_stud(stud:Estudiante):
    stud.id = str(uuid4()) #Pedimos que antes nos genere un id de forma string del estudiante que estamos creando
    estud.append(stud)#Convertimos a diccionario la información que se agrega en la lista
    return "Estudiante agregado con exito" #Retornamos un mensaje

#Busqueda de Estudiantes con for sin query

@app.get("/studs/{id}")
async def get_stud(id:str):
    for estudiante in estud:
        if estudiante.id == id: #Verificamos si el id es igual al que ingresamos
            return estudiante #Retornamos la información que concuerda
    return {"message":"Estudiante no encontrado"}

#Busqueda de estudiantes con lambda

@app.get("/student/{id}")
async def get_studi(id:str):
    srt = filter(lambda us: us.id == id, estud) #Filtramos la lista y en lugar de for creamos una función anónima
    try:
        return list (srt)[0] #Regresamos una lista
    except:
        return {"message":"Estudiante no encontrado"}