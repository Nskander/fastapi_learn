from sqlalchemy import Boolean, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType
import datetime

from game_blog.database import Base


class Post(Base):
    __tablename__ = "posts"

    uid = Column(UUIDType, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_id = Column(Integer, ForeignKey("users.uid"))

    owner = relationship("User", back_populates="post")


