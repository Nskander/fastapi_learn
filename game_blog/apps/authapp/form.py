from typing import List, Optional
from sqlalchemy.orm import Session

from ...core.hashing import Hasher
from ...core.request_framework import PostRequest

from .models import User
from fastapi import Request

class UserForm:
    def __int__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None

    async def load_data(self):
        pass

    async def is_valid(self):
        return True

    async def validate_username(self, db: Session):
        user = db.query(User).filter(User.username == self.username).first()

        if user:
            self.errors.append(
                f'User with username {self.username} has already'
            )



