
from fastapi import FastAPI, Request
from router import user, article
from auth import authentication
from db import models
from db.database import engine
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(article.router)


@app.get('/')
def index():
    return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)

origins = [
  'http://127.0.0.1:5000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory="files"), name='files')