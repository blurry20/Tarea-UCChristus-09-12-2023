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
