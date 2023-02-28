from fastapi import FastAPI
from pydantic import BaseModel #Modelode de Clase
from typing import List  # Libreria para List
from uuid import uuid4  # Para generar los id's de forma aleatoria

# CRUD
app = FastAPI()

# Damos la bienvenidad


@app.get("/")
async def hola():
    return "Bienvenido al CRUD de los Estudiantes"

# Almacenamos en la lista, para no almacenar en base de datos

estud = []

# Clase de los datos del Estudiante


class Estudiante(BaseModel):
    id: str
    nom: str
    apell: str
    edad: int
    habi: List[str] = []

# Metódo post para agregar a la lista los estudiantes


@app.post("/studes", tags=['Bienvenida'])
async def add_stud(stud: Estudiante):
    # Pedimos que antes nos genere un id de forma string del estudiante que estamos creando
    stud.id = str(uuid4())
    estud.append(stud)  # La información se agrega en la lista
    return "Estudiante agregado con exito"  # Retornamos un mensaje

# Metódo GET para visualizar la lista de estudiantes


@app.get("/studs", tags=['Visualización de todos los estudiantes'])
async def studs():
    return estud

#Busqueda de Estudiantes con for sin query


@app.get("/studs/{id}", tags=['Busquedad con for'])
async def get_stud(id:str):
    for estudiante in estud:
        if estudiante.id == id: #Verificamos si el id es igual al que ingresamos
            return estudiante #Retornamos la información que concuerda
        else:
            return {"message": "Estudiante no encontrado"}

#Busqueda de estudiantes con lambda


@app.get("/student/{id}", tags=['Busqueda con Lambda'])
async def get_studi(id:str):
    srt = filter(lambda us: us.id == id, estud) #Filtramos la lista y en lugar de for creamos una función anónima
    try:
        return list (srt)[0] #Regresamos una lista
    except:
        return {"message":"Estudiante no encontrado"}

# El metodo put actualiza o da update


@app.put("/update/{id}", tags=['Actualizar'])
# Como parametros el objeto y la clase, además del ID
async def update(stud: Estudiante, id: str):
    for estudiante in estud:
        if estudiante.id == id:
            estudiante.nom = stud.nom
            estudiante.apell = stud.apell
            estudiante.edad = stud.edad
            estudiante.habi = stud.habi
            return "Estudiante actualizado con exito"
        else:
            return {"message": "Estudiante no encontrado"}

# Update metódo put recorrido de lista con función anónima


@app.put("/update1/{id}", tags=["Aztualizar con lambda"])
# Tanto para agregar como para actualizar usamos como parametros el objeto que se va a crear y l clase
async def update_std(id: str, stud: Estudiante):
    srt = filter(lambda x: x.id == id, estud)
    srt.nom = stud.nom
    srt.apell = stud.apell
    srt.edad = stud.edad
    srt.habi = stud.habi
    return {"message": "Estudiante no encontrado"}  # !No Actualiza

# Metódo Delete mediante path y for


@app.delete("/delete/{id}", tags=['Delete con For'])
async def delete(id: str):
    for l in estud:
        if l.id == id:
            estud.remove(l)
        return "Estudiante eliminado con exito"

# Metódo Delete mediante path y lambda


@app.delete("/delete1/{id}", tags=['Delete con lambda'])
async def delete_std(id: str):
    del_usr = filter(lambda x: x.id == id, estud)
    if del_usr == True:
        estud.remove(del_usr)
