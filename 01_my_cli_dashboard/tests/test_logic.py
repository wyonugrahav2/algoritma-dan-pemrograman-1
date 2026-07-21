from src.logic.analytics import calculate_balance

def test_balance():
    data = [
        {'type': 'income', 'amount': 100000},
        {'type': 'expense', 'amount': 20000}
    ]
    assert calculate_balance(data) == 80000