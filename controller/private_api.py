import json
from http.client import HTTPException
from urllib.request import Request, urlopen

from dotenv import dotenv_values
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt
from starlette.responses import JSONResponse, Response

from model.user_interaction_model import UserInteraction
from model.user_model import User

from service.stats_service import compute_stat
from view_model.user_interaction_viewmodel import UserInteractionViewModel
from view_model.user_viewmodel import UpdateUserViewModel

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


def decode_jwt(token: str):
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
            return payload
    raise HTTPException(status_code=401, detail="invalid_header")


@app_private.middleware("http")
async def verify_user_agent(request: Request, call_next):
    token = request.headers['Authorization']
    payload = decode_jwt(token)
    response = await call_next(request)
    return response



@app_private.get("/users")
async def get_users():
    try:
        streamers = get_users()
        return streamers
    except:
        raise HTTPException(status_code=404, detail="Users not found")


@app_private.get("/user/{user_login}")
async def user(user_login: str, Authorization = Header(...)):
    try:
        token = decode_jwt(Authorization)
        nickname = token['https://brstreamers.dev/nickname']
        if(nickname == user_login):
            streamer = get_user_by_login(user_login)
            return streamer
        
        raise HTTPException(status_code=403, detail="Unauthorized")
    except:
        raise HTTPException(status_code=404, detail="Streamer not found")


@app_private.post("/user")
async def save_user(user: UpdateUserViewModel, Authorization = Header(...)):
    token = decode_jwt(Authorization)
    nickname = token['https://brstreamers.dev/nickname']

    if(nickname == user.user_login):    
        return create_user_model(user)
    raise HTTPException(status_code=403, detail="Unauthorized")  
        

@app_private.put("/user")
async def update_user(user: UpdateUserViewModel, Authorization = Header(...)):
    token = decode_jwt(Authorization)
    nickname = token['https://brstreamers.dev/nickname']

    if(nickname == user.user_login):    
        res = update_user_model(user)
        return res
    raise HTTPException(status_code=403, detail="Unauthorized")  

@app_private.delete("/user/{user_login}")
async def delete_streamer(user_login, Authorization = Header(...)):
    token = decode_jwt(Authorization)
    nickname = token['https://brstreamers.dev/nickname']
    try:
        if(nickname == user_login):
            user = delete_user(user_login)
            return user
        raise HTTPException(status_code=403, detail="Unauthorized")  

    except:
        raise HTTPException(status_code=404, detail="Streamer not found")


@app_private.post("/userinteraction")
async def stats(stat: UserInteractionViewModel, Authorization = Header(...)):
    token = decode_jwt(Authorization)
    nickname = token['https://brstreamers.dev/nickname']
    if(nickname == stat.user_login):
        return compute_stat(stat)
    raise HTTPException(status_code=403, detail="Unauthorized")  


    
@app_private.get("/userinteraction/{user_login}")
async def stats(user_login, Authorization = Header(...)):
    token = decode_jwt(Authorization)
    nickname = token['https://brstreamers.dev/nickname']
    if(nickname == user_login):
        user_interactions = get_user_interactions_by_user_login(user_login)
        data = []
        for interaction in user_interactions:
            data.append(interaction.__data__)
        return data
    raise HTTPException(status_code=403, detail="Unauthorized")  