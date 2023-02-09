from fastapi import FastAPI 
from pydantic import BaseModel 

app = FastAPI()

class Usuario(BaseModel):
    name : str
    apellido : str
    edad : int
    
Usuarios_lista = [Usuario(name="Alberto", apellido="Palma", edad = 38),
                  Usuario(name="Sandra", apellido="Téllez", edad=42)]

@app.get("/userjson")
async def userjson():
    return "Betito"

@app.get("/user")
async def users():
    return Usuarios_lista