
import json

with open("config/rules.json") as f:
    rules = json.load(f)["rules"]

def evaluate_rules(data):
    for rule in rules:
        field = rule["field"]
        operator = rule["operator"]
        value = rule["value"]

        if operator == "<" and data[field] < value:
            return rule["action"], rule["name"]

        if operator == "==" and data[field] == value:
            return rule["action"], rule["name"]

    return "approve", "default_pass"
