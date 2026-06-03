from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from .database import Base, engine
from .routers.autor import router as autor_router
from .routers.livro import router as livro_router

app = FastAPI(
    title="BookStore API",
    description="Sistema de Gerenciamento de Biblioteca Digital",
    version="1.0"
)


@app.on_event("startup")
def on_startup():
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as e:
        print("Aviso: não foi possível conectar ao banco de dados na inicialização:", e)


app.include_router(autor_router)
app.include_router(livro_router)
