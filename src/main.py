from fastapi import FastAPI
from database import init_db
from routers import author_router

init_db()
app = FastAPI()
app.include_router(author_router.router)
