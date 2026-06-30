from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import *
from models import *
from schemas import Register
from security import *


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HandsOn 9"
)

# JWT Auth
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login/"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


# Current user
def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    payload = decode_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = db.query(User).filter(
        User.email == payload["sub"]
    ).first()

    return user


# Home
@app.get("/")
def home():

    return {
        "message": "API Running"
    }


# REGISTER
@app.post(
    "/api/v1/auth/register/",
    status_code=201
)
def register(

    user: Register,

    db: Session = Depends(get_db)

):

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = User(

        email=user.email,

        hashed_password=
        get_password_hash(
            user.password
        )

    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User registered"
    }


# LOGIN
@app.post(
    "/api/v1/auth/login/"
)
def login(

    form_data:
    OAuth2PasswordRequestForm =
    Depends(),

    db: Session =
    Depends(get_db)

):

    user = db.query(User).filter(
        User.email ==
        form_data.username
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Wrong Email"
        )

    if not verify_password(

        form_data.password,

        user.hashed_password

    ):

        raise HTTPException(
            status_code=401,
            detail="Wrong Password"
        )

    token = create_access_token(

        {
            "sub":
            user.email
        }

    )

    return {

        "access_token":
        token,

        "token_type":
        "bearer"
    }


# PROTECTED
@app.post(
    "/api/v1/courses/"
)
def create_course(

    current_user=
    Depends(
        get_current_user
    )

):

    return {

        "message":
        "Course created"
    }


# PUBLIC
@app.get(
    "/api/v1/courses/"
)
def get_courses():

    return [

        "Python",

        "FastAPI"
    ]