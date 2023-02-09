from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "!Hola FastAPi¡"

@app.get("/url")
async def root():
    return {"Nombre":"Alberto", "Apellido":"Palma"}

