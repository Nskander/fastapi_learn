from sqlalchemy import Boolean, Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, UUIDType
import datetime
from uuid import uuid4

from db.base_class import Base


class Post(Base):

    uid = Column(UUIDType, primary_key=True, default=uuid4)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    is_active = Column(Boolean, default=True)
    title = Column(String)
    content = Column(String)
    owner_uid = Column(UUIDType, ForeignKey("user.uid"))

    owner = relationship("User", back_populates="post")


