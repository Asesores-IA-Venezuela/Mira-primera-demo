from fastapi import FastAPI
app = FastAPI()

class User():
    name: str
    lastname: str
    email: str
    age: int

usersDB = [user()]
@app.get("/usersjson")
async def usersJson():
    return "Hello users!!"