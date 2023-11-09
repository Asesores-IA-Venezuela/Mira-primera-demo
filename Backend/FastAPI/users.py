from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    lastname: str
    url: str
    age: int

usersDB = [User("Moises", "Ochoa", "moisesochoa_20@hotmail.com", 22),
           User("Samuel", "Sanchez", "smuel45454@gamil.com,", 25)]


@app.get("/users")
async def get_users():
    return usersDB

