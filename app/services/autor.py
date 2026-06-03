from fastapi import HTTPException

from app.database import SessionLocal
from app.models import Autor
from app.schemas import AutorCreate


def criar_autor(autor: AutorCreate):
    db = SessionLocal()
    novo_autor = Autor(
        nome=autor.nome,
        nacionalidade=autor.nacionalidade,
        data_nascimento=autor.data_nascimento
    )
    db.add(novo_autor)
    db.commit()
    db.refresh(novo_autor)
    db.close()
    return novo_autor


def listar_autores():
    db = SessionLocal()
    autores = db.query(Autor).all()
    db.close()
    return autores


def buscar_autor(autor_id: int):
    db = SessionLocal()
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    db.close()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return autor


def atualizar_autor(autor_id: int, dados: AutorCreate):
    db = SessionLocal()
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if not autor:
        db.close()
        raise HTTPException(status_code=404, detail="Autor não encontrado")

    autor.nome = dados.nome
    autor.nacionalidade = dados.nacionalidade
    autor.data_nascimento = dados.data_nascimento

    db.commit()
    db.refresh(autor)
    db.close()
    return autor


def deletar_autor(autor_id: int):
    db = SessionLocal()
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if not autor:
        db.close()
        raise HTTPException(status_code=404, detail="Autor não encontrado")

    db.delete(autor)
    db.commit()
    db.close()
    return
