
from engine.rule_engine import evaluate_rules

def test_approve():
    data = {
        "salary": 60000,
        "credit_score": 700,
        "documents_submitted": True
    }
    decision, _ = evaluate_rules(data)
    assert decision == "approve"

def test_reject():
    data = {
        "salary": 20000,
        "credit_score": 700,
        "documents_submitted": True
    }
    decision, _ = evaluate_rules(data)
    assert decision == "reject"
