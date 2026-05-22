from fastapi import FastAPI
from .core.config import settings
from .db.database import engine
from .db.models import Base
from app.api.routes import router as user_router
from app.api.auth_routes import router as auth_router


Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)
app.include_router(user_router)
app.include_router(auth_router)