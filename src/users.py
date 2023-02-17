from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hola banda"}
    
#Se define una clase para el modelo
class Usuario(BaseModel):
    id : int
    name : str
    apellido : str
    edad : int
#Se crea una lista de usuarios
Usuarios_lista = [Usuario(id = 1, name="Alberto", apellido="Palma", edad = 38),
                  Usuario(id = 2,name="Sandra", apellido="Téllez", edad=42)]

@app.get("/userjson")
async def userjson():
    return "Betito"

@app.get("/user")
async def users():
    #Se devuelve la lista de usuarios
    return Usuarios_lista

#Se pasan parametros
@app.get("/items/{algo}")
async def item(algo):
    return {"items": algo}

#Path completo
@app.get("/users/{id}")
async def user(id:int):
    usrs = filter(lambda u: u.id == id,Usuarios_lista)
    try:
        return list (usrs)[0]
    except:
        return {"message":"Usuario no encontrado"}
       
#Query manda imprime el nombre de un usuario  
@app.get("/userquery/")
async def userquery(id:int):
    usrs = filter(lambda u: u.id == id,Usuarios_lista)
    try:
        return list (usrs)[0].name
    except:
        return {"message":"Usuario no encontrado"}
    
#Query manda imprimir los datos de un usuario
    
@app.get("/userquery2/")
async def userquery2(id:int):
    usrs = filter(lambda r: r.id == id,Usuarios_lista)
    try:
        return list (usrs)[0]
    except:
        return {"message":"Usuario no encontrado"}