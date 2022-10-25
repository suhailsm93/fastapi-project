from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schema, utils
from . database import engine, get_db
from sqlalchemy.orm import Session
from typing import Optional, List
from . routers import post, user, auth, vote 
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

origins=["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# while True:
#     try:
#         conn=psycopg2.connect(host='localhost', database='postgres', user='postgres',
#          password='batmandarkknight', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection Sucessful!")
#         break
        
#     except Exception as error:
#         print("Connection to Database Failed")
#         print("Error:",error)
#         time.sleep(2)
    

# my_posts= [{"title":"title of first post", "content":"content of first post", "id":1},{"title":"title for second post", "content":"content for second post", "id":2}]

# def find_post(id):
    # for p in my_posts:
    #     if p['id']==id:
    #         return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id']==id:
#             return i

# @app.get("/")
# def root():
#     return{"message":"hello world"}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)