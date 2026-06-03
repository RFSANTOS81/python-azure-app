from app.services.autor import criar_autor, listar_autores, buscar_autor, atualizar_autor, deletar_autor
from app.services.livro import criar_livro, listar_livros, buscar_livro, atualizar_livro, deletar_livro


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


def criar_livro(livro: LivroCreate):
    db = SessionLocal()
    autor = db.query(Autor).filter(Autor.id == livro.autor_id).first()
    if not autor:
        db.close()
        raise HTTPException(status_code=404, detail="Autor não encontrado")

    novo_livro = Livro(
        titulo=livro.titulo,
        ano_publicacao=livro.ano_publicacao,
        genero=livro.genero,
        autor_id=livro.autor_id
    )
    db.add(novo_livro)
    db.commit()
    db.refresh(novo_livro)
    db.close()
    return novo_livro


def listar_livros():
    db = SessionLocal()
    livros = db.query(Livro).all()
    db.close()
    return livros


def buscar_livro(livro_id: int):
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    db.close()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


def atualizar_livro(livro_id: int, dados: LivroCreate):
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        db.close()
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    autor = db.query(Autor).filter(Autor.id == dados.autor_id).first()
    if not autor:
        db.close()
        raise HTTPException(status_code=404, detail="Autor não encontrado")

    livro.titulo = dados.titulo
    livro.ano_publicacao = dados.ano_publicacao
    livro.genero = dados.genero
    livro.autor_id = dados.autor_id

    db.commit()
    db.refresh(livro)
    db.close()
    return livro


def deletar_livro(livro_id: int):
    db = SessionLocal()
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro:
        db.close()
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    db.delete(livro)
    db.commit()
    db.close()
    return
