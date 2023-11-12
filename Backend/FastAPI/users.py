from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
app.title = "API gestión de usuarios"
app.version = "0.0.1"
#Para colocar tags, ir a la ruta y poner tags=["Lo que aplique"]
class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int

#Conectar con BD de usuarios
usersDB = [User(id=1,name="Moises", lastname="Ochoa", url="moisesochoa_20@hotmail.com", age=22),
           User(id=2,name="Samuel", lastname="Sanchez", url="smuel45454@gamil.com,", age=25)]

#get con Path para el listado de usuarios
@app.get("/users")
async def get_users():
    return usersDB

#get con Path para llamar a un solo usuario con id
@app.get("/user/{id}")
async def get_individualuser(id: int):
    return searchUser(id)

#get con Query para llamar a un solo usuario con id
@app.get("/userquery")
async def get_individualuser(id: int):
    return searchUser(id)

def searchUser(id: int):
    user = next((u for u in usersDB if u.id == id), None)
    if user is not None:
        return user
    else:
        return {"error": "No se ha encontrado el usuario"}
    
#Insetar usuarios, sin que sean repetidos  
@app.post("/users")
async def user(user: User):
    if type (searchUser(user.id))== User:
        return {"error": "El Usuario ya existe"}
    usersDB.append(user)
    return user

#Actualizar datos de un usuario
@app.put("/users")
async def user(user: User):
    found = False
    for index, usersave in enumerate(usersDB):
        if usersave.id == user.id:
            usersDB[index] = user
            found = True
    if found:
        return user
    else:
        return {"error": "no se ha logrado actualizar el usuario"}
    
#Eliminar un usuario según su id
@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, usersave in enumerate(usersDB):
        if usersave.id == id:
           del usersDB[index]
           found=True   
    if found:
        return id
    else:
        return {"error": "no se ha logrado eliminar el usuario"}
        

