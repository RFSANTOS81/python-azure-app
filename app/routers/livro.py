from fastapi import APIRouter

from app.services.livro import criar_livro, listar_livros, buscar_livro, atualizar_livro, deletar_livro
from app.schemas import LivroCreate, LivroResponse

router = APIRouter(prefix="/livros", tags=["livros"])


@router.post("", response_model=LivroResponse, status_code=201)
def criar_livro(livro: LivroCreate):
    return crud.criar_livro(livro)


@router.get("", response_model=list[LivroResponse])
def listar_livros():
    return crud.listar_livros()


@router.get("/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int):
    return crud.buscar_livro(livro_id)


@router.put("/{livro_id}", response_model=LivroResponse)
def atualizar_livro(livro_id: int, dados: LivroCreate):
    return crud.atualizar_livro(livro_id, dados)


@router.delete("/{livro_id}", status_code=204)
def deletar_livro(livro_id: int):
    return crud.deletar_livro(livro_id)
