from fastapi import FastAPI
from routers.routes import router as NoteRouter

app = FastAPI()

app.include_router(NoteRouter, prefix="/api/py/note")