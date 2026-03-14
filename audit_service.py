
from storage.database import audit_logs
from datetime import datetime

def log_audit(app_id, decision, rule):
    audit_logs.append({
        "application_id": app_id,
        "decision": decision,
        "rule_triggered": rule,
        "timestamp": str(datetime.now())
    })
