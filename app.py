from datetime import datetime
from pydantic import BaseModel
from uuid import uuid4 as uuid
from typing import Text, Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False


@app.get('/')
def read_root():
    return {"welcome":"Welcome to my REST API"}

@app.get('/posts')
def get_posts():
    return posts

@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404,detail="Post Not Found")
    

@app.post('/posts')
async def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for key, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(key)
            return {"message": "Post Eliminado Correctamente"}
    raise HTTPException(status_code=404,detail="Post Not Found")

@app.put('/posts/{post_id}')
def update(post_id: str, updatedPost: Post):
    for id, post in enumerate(posts):
        if post["id"] == post_id:
            posts[id]["title"] = updatedPost.title
            posts[id]["author"] = updatedPost.author
            posts[id]["content"] = updatedPost.content
            return {"message": "Post Actualizado Correctamente"}
    raise HTTPException(status_code=404,detail="Post Not Found")
