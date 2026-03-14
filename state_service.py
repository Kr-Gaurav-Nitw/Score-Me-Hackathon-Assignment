
from storage.database import applications

def update_state(app_id, state):
    if app_id not in applications:
        applications[app_id] = []
    applications[app_id].append(state)
