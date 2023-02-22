
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
#Query con for en lugar de filter  
@app.get("/userquery3/")
async def userquery3(id:int):
    for l in Usuarios_lista:
        if l.id == id:
            return l
        else:
            return {"message":"Usuario no encontrado"} 
         
#Query para operaciones
@app.get("/calculadora")
async def calculadora(a:int,b:int):
    return a+b

@app.get('/multi')
async def multi(a : int, b :int):
    return {"El resultado es":a*b}

#Busqueda con lambda

def sear_user(id:int):
    usr = filter(lambda u: u.id == id,Usuarios_lista)
    try:
        return list (usr)[0]
    except:
        return {"message":"Usuario no encontrado"}
#Post con lambda
@app.post("/user")
async def post_user(usuario:Usuario):
        if type(sear_user(usuario.id)) == Usuario:
            return {"message":"Usuario ya existe"}
        else:
            Usuarios_lista.append(usuario)
            return {"message":"Usuario creado"}
        
#post con for
@app.post("/usersearch")
async def post_usersearch(usuario:Usuario):
    if type(user_search(usuario.id)) == Usuario:
        return {"message":"Usuario ya existe"}
    else:
        Usuarios_lista.append(usuario)
        return {"message":"Usuario creado"}
    
#Busqueda con for
def user_search(id:int):
    for l in Usuarios_lista:
        if l.id == id:
            return {"message":"El usuario ya existe"}
        else:
            Usuarios_lista.append()
            return {"message":"Usuario creado"}
#Método Post

@app.post('/students')
async def save(name:str, lastname:str):
    return "Estudiante {} {} ha sido guardado".format(name, lastname)

#Metodo post Clase Basemodel

class Student(BaseModel):
    name : str
    lastname: str
    age: int
    
@app.post('/students2')
async def stud(studiante:Student):
    return "Estudiante {} {} ha sido guardado con la edad de {} años".format(studiante.name, studiante.lastname, studiante.age)

