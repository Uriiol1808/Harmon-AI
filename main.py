from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Allow both localhost and 127.0.0.1 as origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the Vue app as a static folder
app.mount("/static", WSGIMiddleware(StaticFiles(directory="frontend/dist", html=True)))

@app.get("/")
def read_root():
    return {"Hello": "World"}