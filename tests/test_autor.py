from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app import app

client = TestClient(app)

def test_criar_autor_sucesso():
    resposta = client.post("/autores/criar/", json={
        "nome": "Teste Autor",
        "pais_origem": "Brasil"
    })
    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["nome"] == "Teste Autor"
    assert dados["pais_origem"] == "Brasil"
    assert "id" in dados


def test_criar_autor_falha_sem_pais():
    resposta = client.post("/autores/criar/", json={
        "nome": "Sem País"

    })
    assert resposta.status_code == 422  