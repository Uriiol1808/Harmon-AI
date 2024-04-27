# import uvicorn

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, BinaryIO

from .sentiment_processing import SentimentProcessing


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/sentiment-prediction/")
async def sentiment_prediction(file: UploadFile = File(...)):
    # Read file content
    contents = await file.read()
    content_string = contents.decode('utf-8')
    
    # Process text into token vector
    token_vector = SentimentProcessing.lyrics_processing(content_string)

    # Make the prediction
    prediction = SentimentProcessing.model_evaluation(token_vector)
    
    return JSONResponse(content={"prediction": prediction, "name": file.filename})
