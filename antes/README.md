# CredNova Credit API

API simples para cálculo de limite de crédito.

## Executar

docker compose up --build

## Endpoint

POST /credit-limit

Exemplo:

{
  "cpf": "123.456.789-00",
  "income": 5000,
  "score": 850
}
