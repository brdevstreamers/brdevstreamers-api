from http.client import HTTPException
import json
from urllib.request import Request, urlopen
from fastapi import FastAPI
from dotenv import dotenv_values
from jose import jwt
from starlette.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from model.user_model import User
from view_model.user_viewmodel import UserViewModel


origins = ["*"]


config = dotenv_values(".env")
app_private = FastAPI(openapi_prefix="/api")

app_private.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


AUTH0_DOMAIN = 'zapperson.us.auth0.com'
API_AUDIENCE = "BrStreamersApi"
ALGORITHMS = ["RS256"]


@app_private.middleware("http")
async def verify_user_agent(request: Request, call_next):
    token = request.headers['Authorization']
    token = token.split(" ")[1]
    jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise HTTPException(status_code=401, detail="token_expired")
            except jwt.JWTClaimsError:
                raise HTTPException(status_code=404, detail="invalid_claims")
                
            except Exception:
                raise HTTPException(status_code=401, detail="invalid_header")
    if payload is not None:
            response = await call_next(request)
            return response
    raise HTTPException(status_code=401, detail="invalid_header")




@app_private.get("/users")
async def get_users():
    try:
        streamers = User.select().get()
        return streamers
    except:
        raise HTTPException(status_code=404, detail="Users not found")


@app_private.get("/user/{user_login}")
async def user(user_login: str):
    try:
        return User.select().where(User.user_login == user_login).get()
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")


@app_private.post("/user")
async def save_user(user: UserViewModel):
    return User.create(
        user_login=user.user_login,
        email=user.email,
        bio=user.bio,
        discord = user.discord,
        instagram = user.instagram,
        linkedin = user.linkedin,
        github = user.github,
        twitter = user.twitter)
        

@app_private.put("/user")
async def update_user(user: UserViewModel):
    res = (User
       .update({User.instagram: user.instagram,
                User.linkedin: user.linkedin,
                User.github: user.github,
                User.twitter: user.twitter,
                User.discord: user.discord,
                User.bio: user.bio
                })
       .where(User.user_login == user.user_login)
       .execute())
    return res
        

@app_private.delete("/user/{user_login}")
async def delete_streamer(user_login):
    try:
        user = User.delete().where(User.user_login == user_login).execute()
        return user
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")

