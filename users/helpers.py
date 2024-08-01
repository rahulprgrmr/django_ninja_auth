from typing import Any
from django.http import HttpRequest
from ninja.security import HttpBearer

from users.models import Token

class TokenAuth(HttpBearer):
    def authenticate(self, request: HttpRequest, token: str) -> Any | None:
        if not Token.objects.filter(key=token).exists():
            return False
        token = Token.objects.filter(key=token).first()
        return token.user