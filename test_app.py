import pytest
from app import app

@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as cliente:
        yield cliente

def test_pagina_inicio(cliente):
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200

def test_endpoint_salud(cliente):
    respuesta = cliente.get("/salud")
    datos = respuesta.get_json()
    assert datos["status"] == "ok"