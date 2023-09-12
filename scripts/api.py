import os
import sqlite3
from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware


app = FastAPI()

static_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../static")

middleware = [
    Middleware(CORSMiddleware, allow_origins=[
               "*"], allow_methods=["*"], allow_headers=["*"])
]

app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, "index.html"))


def conexion_db():
    try:
        conn = sqlite3.connect("MOCK_DATA.db")
        return conn
    except sqlite3.Error as error:
        print("Error al conectar con la base de datos", error)
        return None


@app.get("/buscar/id/{id}")
def buscar_por_rut(id: int):
    conn = conexion_db()
    if conn is None:
        return JSONResponse(content={"error": "Error al conectar con la base de datos"}, status_code=500)

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM datos WHERE id=?''', (id,))
            datos = cursor.fetchall()

            if datos:
                usuarios = [{
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "gender": row[4],
                    "Plan de Salud": row[5],
                    "phone": row[6]}
                    for row in datos]
                return {"usuarios": usuarios}
            else:
                return JSONResponse(content={"error": "No se encontró el usuario"}, status_code=404)
    except sqlite3.Error as error:
        return JSONResponse(content={"error": str(error)}, status_code=500)


@app.get("/buscar/email/{email}")
def buscar_por_email(email: str):
    conn = conexion_db()
    if conn is None:
        return JSONResponse(content={"error": "Error al conectar con la base de datos"}, status_code=500)

    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM datos WHERE email = ?''', (email,))
            datos = cursor.fetchall()

            if datos:
                usuarios = [{
                    "id": row[0],
                    "first_name": row[1],
                    "last_name": row[2],
                    "email": row[3],
                    "gender": row[4],
                    "Plan de Salud": row[5],
                    "phone": row[6]}
                    for row in datos]
                return {"usuarios": usuarios}
            else:
                return JSONResponse(content={"error": "No se encontró el usuario"}, status_code=404)
    except sqlite3.Error as error:
        return JSONResponse(content={"error": str(error)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
