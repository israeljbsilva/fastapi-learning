from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel, Extra
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from microblog.models.user import User


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    user_id: Optional[int] = Field(foreign_key='user.id')
    user: Optional['User'] = Relationship(back_populates='posts')

    def __lt__(self, other):
        return self.date < other.date


class PostResponse(BaseModel):
    id: int
    text: str
    date: datetime
    user_id: int


class PostRequest(BaseModel):
    date: datetime
    text: str

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True
