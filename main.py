from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Mount the Vue app as a static folder
app.mount("/static", WSGIMiddleware(StaticFiles(directory="frontend/dist", html=True)))

@app.get("/")
def read_root():
    return {"Hello": "World"}