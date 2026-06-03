from fastapi import APIRouter

from app.services import autor as autor_service
from app.schemas import AutorCreate, AutorResponse

router = APIRouter(prefix="/autores", tags=["autores"])


@router.post("", response_model=AutorResponse, status_code=201)
def criar_autor(autor: AutorCreate):
    return autor_service.criar_autor(autor)


@router.get("", response_model=list[AutorResponse])
def listar_autores():
    return autor_service.listar_autores()


@router.get("/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int):
    return autor_service.buscar_autor(autor_id)


@router.put("/{autor_id}", response_model=AutorResponse)
def atualizar_autor(autor_id: int, dados: AutorCreate):
    return autor_service.atualizar_autor(autor_id, dados)


@router.delete("/{autor_id}", status_code=204)
def deletar_autor(autor_id: int):
    return autor_service.deletar_autor(autor_id)
