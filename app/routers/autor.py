from fastapi import APIRouter

from app.services.autor import criar_autor, listar_autores, buscar_autor, atualizar_autor, deletar_autor
from app.schemas import AutorCreate, AutorResponse

router = APIRouter(prefix="/autores", tags=["autores"])


@router.post("", response_model=AutorResponse, status_code=201)
def criar_autor(autor: AutorCreate):
    return crud.criar_autor(autor)


@router.get("", response_model=list[AutorResponse])
def listar_autores():
    return crud.listar_autores()


@router.get("/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int):
    return crud.buscar_autor(autor_id)


@router.put("/{autor_id}", response_model=AutorResponse)
def atualizar_autor(autor_id: int, dados: AutorCreate):
    return crud.atualizar_autor(autor_id, dados)


@router.delete("/{autor_id}", status_code=204)
def deletar_autor(autor_id: int):
    return crud.deletar_autor(autor_id)
