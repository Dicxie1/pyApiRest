from application import mydb, mycurso
from json import dumps, loads
mycurso.execute("SELECT * FROM Alumno")
result = mycurso.fetchall()

jsonObjet = dumps(result, indent=4, sort_keys=True, default=str)
jsonArray = loads(jsonObjet)
print(jsonObjet)
print("conversion a arreglo")
print(jsonArray[0])
