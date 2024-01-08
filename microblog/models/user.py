from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship

from pydantic import BaseModel


if TYPE_CHECKING:
    from microblog.models.post import Post


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: str = Field(nullable=False)
    posts: List['Post'] = Relationship(back_populates='user')


class UserResponse(BaseModel):
    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserRequest(BaseModel):
    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
