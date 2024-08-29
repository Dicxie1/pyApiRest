import mysql.connector 
from pydantic import BaseModel
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