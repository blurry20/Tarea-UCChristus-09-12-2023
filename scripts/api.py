import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware


app = FastAPI()

static_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "../static")

middleware = [
    Middleware(CORSMiddleware, allow_origins=[
               "*"], allow_methods=["*"], allow_headers=["*"])
]
