from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Allow both localhost and 127.0.0.1 as origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the Vue app as a static folder
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/message")
def get_message():
    return {"message": "Hello from FastAPI!"}