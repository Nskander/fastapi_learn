from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from game_blog.apps.mainapp.routes import router

from .database import engine

from game_blog.apps import authapp, postsapp
from .apps.authapp import models
from .apps.postsapp import models

authapp.models.Base.metadata.create_all(bind=engine)
postsapp.models.Base.metadata.create_all(bind=engine)


def create_app(debug=True):
    app = FastAPI(debug=debug)
    app.mount('/static', StaticFiles(directory='game_blog/static'), name='static')
    app.include_router(router)
    return app