import requests
from app.core.config import settings


class GoogleAuthService:

    def get_auth_url(self):
        return (
            "https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={settings.GOOGLE_CLIENT_ID}"
            f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
            "&response_type=code"
            "&scope=openid%20email%20profile"
            "&access_type=offline"
            "&prompt=consent"
        )

    def get_token(self, code: str): 
        token_url = "https://oauth2.googleapis.com/token"

        data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        response = requests.post(token_url, data=data)
        return response.json() # return the entire response for better error handling

    def get_user_info(self, access_token: str):
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers=headers
        )

        return response.json()