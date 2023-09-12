# Tarea-UCChristus-09-12-2023
Tarea enviada para evaluacion de practica

#Configuracion
1. Clone el repositorio.


2.-Primero se debe instalar fastapi con el comando `pip install fastapi`


3.-Se debe entrar a la carpeta de script a traves de la terminal es decir: `cd ../../Tarea-UCChristus-09-12-2023/scripts`


4.-Una vez ahi en caso de que la base de datos no este poblada o creada, se ejecuta el script (se debe estar dentro de la carpeta scripts) con el comando `python importar_datos.py` (Para probar el script se puede borrar la base de datos y ejecutarlo)


5.-Luego se ejecuta el comando `pip install uvicorn` para inciar la aplicacion


6.- Luego dentro de la carpeta scripts se ejecuta el siguiente comando `uvicorn api:app --host 0.0.0.0 --port 8000 --reload` este ejecutara la aplicacion en la url `http://localhost:8000/`
