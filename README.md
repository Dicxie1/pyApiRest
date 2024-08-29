# API Rest con Python

## Descripción
el proyecto api rest de la aplicación de svelte
## Prerequisitos
- mysql-connector-python
- uvicorn   0.30.0
- fastapi  0.112.2
- pydantic  2.8.2
- urllib3 1.26.6
- resquest 2.32.3

## Configurar
Crear el Entorno virtual  
```console
python3 venv apirest
cd apirest/
```
iniciar el entorno virtual 
```console
source bin/active
```
Instalar las dependeicias 
```console
pip install urllib3 request mysql-connector-python fastapi pydantic
```

## Iniciar
```console
npm uvicorn application:app 
```