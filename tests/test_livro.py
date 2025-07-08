from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app import app


client = TestClient(app)

def test_criar_livro_sucesso():
    # Primeiro cria um autor (FK)
    autor_resp = client.post("/autores/criar/", json={
        "nome": "Autor do Livro",
        "pais_origem": "Portugal"
    })
    autor_id = autor_resp.json()["id"]

    resposta = client.post("/livros/criar/", json={
        "titulo": "Livro de Teste",
        "ano_publicacao": 2020,
        "editora": "Editora Teste",
        "disponivel": True,
        "autor_id": autor_id
    })

    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["titulo"] == "Livro de Teste"
    assert dados["disponivel"] == True
    assert "isbn" in dados


def test_criar_livro_falha_autor_inexistente():
    resposta = client.post("/livros/criar/", json={
        "titulo": "Livro Sem Autor",
        "ano_publicacao": 2021,
        "editora": "Editora X",
        "autor_id": 9999  # Autor que não existe
    })

    # Esperamos erro 500 porque o autor_id 9999 não existe no banco
    assert resposta.status_code in [400, 422, 500]
