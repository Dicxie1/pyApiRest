from fastapi import FastAPI, HTTPException
import mysql.connector 
import requests
from pydantic import BaseModel
import json
from datetime import date

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    db= "Colegio"
)
mycurso = mydb.cursor(dictionary=True)
class AlumnoModel(BaseModel):
    numMatricula: int
    nombre: str
    fechaNacimiento: date
    telefono:int

print(mydb)
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product")
def list_product():
    return {"messge": "List of product"}
@app.get("/product/{product_id}")
async def getProductById(product_id: int):
    return {"productID": product_id}

@app.get("/uno")
def get_uno():
    api_rest = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_rest)
    return response.json()

@app.get("/student")
async def students():
    sQuery = "select * from Alumno"
    mycurso.execute(sQuery)
    result = mycurso.fetchall()
   
    return result

@app.post("/student")
async def update_student(alumno:AlumnoModel):
    sQuery = "INSERT INTO Alumno VALUE(%s,%s,%s,%s)"
    value = (alumno.numMatricula, alumno.nombre, alumno.fechaNacimiento, alumno.telefono)
    try:
        mycurso.execute(sQuery, value)
        mydb.commit()
    except mysql.connector.Error as error:
         raise HTTPException(status_code=400, detail=f"Error: {error}")
    return {"message": "Insert Successfully"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
