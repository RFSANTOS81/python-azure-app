from typing import ClassVar

import pydantic as pyd
from pydantic import BaseModel


def _response_model_config():
    try:
        major = int(pyd.__version__.split(".")[0])
    except Exception:
        major = 1

    if major >= 2:
        return type("Config", (), {"model_config": {"from_attributes": True}})
    else:
        return type("Config", (), {"orm_mode": True})


class AutorCreate(BaseModel):
    nome: str
    nacionalidade: str
    data_nascimento: str


class AutorResponse(BaseModel):
    id: int
    nome: str
    nacionalidade: str
    data_nascimento: str

    Config: ClassVar = _response_model_config()


class LivroCreate(BaseModel):
    titulo: str
    ano_publicacao: int
    genero: str
    autor_id: int


class LivroResponse(BaseModel):
    id: int
    titulo: str
    ano_publicacao: int
    genero: str
    autor_id: int

    Config: ClassVar = _response_model_config()
