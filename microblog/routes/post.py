from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from microblog.db import ActiveSession
from microblog.models.post import (
    Post,
    PostRequest,
    PostResponse,
)
from microblog.models.user import User, UserRequestPost

router = APIRouter()


@router.get('/', response_model=List[PostResponse])
async def list_posts(*, session: Session = ActiveSession):
    posts = session.exec(select(Post)).all()
    return posts


@router.post('/', response_model=PostResponse, status_code=201)
async def create_post(*, session: Session = ActiveSession, user: UserRequestPost, post: PostRequest):
    post.user_id = user.id

    db_post = Post.from_orm(post)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


@router.get('/{post_id}/', response_model=PostResponse)
async def get_post_by_post_id(*, session: Session = ActiveSession, post_id: int):
    query = select(Post).where(Post.id == post_id)
    post = session.exec(query).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get('/user/{username}/', response_model=List[PostResponse])
async def get_posts_by_username(*, session: Session = ActiveSession, username: str):
    query = select(Post).join(User).where(User.username == username)
    posts = session.exec(query).all()
    return posts
