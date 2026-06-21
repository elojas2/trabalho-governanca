from services.credit_service import calculate_credit_limit

def test_high_score():
    assert calculate_credit_limit(850, 1000) == 10000

def test_regular_score():
    assert calculate_credit_limit(700, 1000) == 5000
