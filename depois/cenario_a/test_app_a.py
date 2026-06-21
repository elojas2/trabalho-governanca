import pytest

from app import app




# CPF fictício: válido pelo algoritmo de dígitos verificadores,
# não pertence a nenhuma pessoa real.
VALID_CPF = "835.291.647-55"
INVALID_CHECKSUM_CPF = "835.291.647-00"
REPEATED_DIGITS_CPF = "111.111.111-11"
MALFORMED_CPF = "123.456.789"


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_valid_cpf_returns_masked_cpf_and_limit(client):
    response = client.post("/credit-limit", json={
        "cpf": VALID_CPF,
        "income": 1000,
        "score": 850,
    })

    assert response.status_code == 200
    body = response.get_json()
    assert body["approved_limit"] == 10000
    assert body["cpf"] == "***.***.647-55"
    assert "835" not in body["cpf"]
    assert "291" not in body["cpf"]


def test_invalid_checksum_cpf_is_rejected_with_generic_message(client):
    response = client.post("/credit-limit", json={
        "cpf": INVALID_CHECKSUM_CPF,
        "income": 1000,
        "score": 850,
    })

    assert response.status_code == 400
    body = response.get_json()
    assert "cpf" not in body
    assert INVALID_CHECKSUM_CPF not in body["error"]


def test_repeated_digits_cpf_is_rejected(client):
    response = client.post("/credit-limit", json={
        "cpf": REPEATED_DIGITS_CPF,
        "income": 1000,
        "score": 850,
    })

    assert response.status_code == 400


def test_malformed_cpf_is_rejected(client):
    response = client.post("/credit-limit", json={
        "cpf": MALFORMED_CPF,
        "income": 1000,
        "score": 850,
    })

    assert response.status_code == 400


def test_missing_cpf_is_rejected(client):
    response = client.post("/credit-limit", json={
        "income": 1000,
        "score": 850,
    })

    assert response.status_code == 400
