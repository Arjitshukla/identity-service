from fastapi import FastAPI
from .core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get("/")
def read_root():
    return {"message ": "Oauth Project is working!"}