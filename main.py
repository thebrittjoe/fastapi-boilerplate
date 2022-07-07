from operator import truediv
import uvicorn
from fastapi import Body, FastAPI, Depends
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer

app = FastAPI()

posts = [
    {
        "id": 1,
        "title": "My first blog",
        "text": "Some blog post content",
    },
    {
        "id": 2,
        "title": "My second blog",
        "text": "Some more blog post content",
    }
]


@app.get("/", tags=["test"])
def hello():
    return {"Hello":"World!"}

# get posts

@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

# get single post by id
@app.get("/posts/{id}", tags=["posts"])
def get_post(id: int):
    if id > len(posts):
        return {
            "error": "Post with this ID does not exist!"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }
 
 # add a blog post           
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post : PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post added successfully!"
    }

users = []

    
# User signup [ create an account ]
@app.post("/user/signup", tags=["user"])
def user_signup(user : UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@app.post("/user/login", tags=["user"])
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid login details!"
        }