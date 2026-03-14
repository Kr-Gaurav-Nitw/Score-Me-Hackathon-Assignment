
from engine.rule_engine import evaluate_rules
from services.audit_service import log_audit
from services.state_service import update_state
from services.dependency_service import verify_documents

def process_application(data):

    update_state(data["application_id"], "RECEIVED")

    if not verify_documents():
        update_state(data["application_id"], "RETRY")
        return {"decision": "retry"}

    decision, rule = evaluate_rules(data)

    update_state(data["application_id"], decision.upper())

    log_audit(data["application_id"], decision, rule)

    return {
        "decision": decision,
        "rule_triggered": rule
    }
