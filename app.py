from pydantic import BaseModel
from datetime import datetime
from fastapi import FastAPI
from typing import Text, Optional

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

@app.post('/posts')
async def save_post(post: Post):
    return post