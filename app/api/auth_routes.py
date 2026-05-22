from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app.db.database import get_db
from app.auth.google import GoogleAuthService
from app.crud.user import get_user_by_email, create_user

router = APIRouter()
google_service = GoogleAuthService()


@router.get("/auth/google/login")
def google_login():
    url = google_service.get_auth_url()

    return RedirectResponse(url=url)

@router.get("/auth/google/callback")
def google_callback(code: str, db: Session = Depends(get_db)):

    token_data = google_service.get_token(code)

    if "access_token" not in token_data:
        raise HTTPException(status_code=400, detail=token_data)

    access_token = token_data["access_token"]

    user_info = google_service.get_user_info(access_token)

    email = user_info.get("email")

    user = get_user_by_email(db, email)

    if not user:
        user = create_user(
            db,
            email=email,
            username=user_info.get("name")
        )

    return {
        "message": "Login successful",
        "user": {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "provider": "google"
        }
    }