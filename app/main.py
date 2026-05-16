from fastapi import FastAPI
from .core.config import settings
from .db.database import engine
from .db.models import Base


Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

@app.get("/")
def read_root():
    return {"message": "DB Connected"}