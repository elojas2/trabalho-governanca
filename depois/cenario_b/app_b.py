from flask import Flask, request, jsonify
from services.credit_service import calculate_credit_limit
from services.cpf_validator import is_valid_cpf

app = Flask(__name__)

@app.route("/credit-limit", methods=["POST"])
def credit_limit():
    data = request.json

    cpf = data.get("cpf")
    income = data.get("income")
    score = data.get("score")

    if not is_valid_cpf(cpf):
        return jsonify({"error": "invalid cpf"}), 400

    limit = calculate_credit_limit(score, income)

    return jsonify({
        "cpf": cpf,
        "approved_limit": limit
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
