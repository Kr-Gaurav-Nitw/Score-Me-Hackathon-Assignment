
from fastapi import FastAPI
from models.request_model import ApplicationRequest
from engine.workflow_engine import process_application
from storage.database import applications

app = FastAPI()

@app.post("/process")
def process(request: ApplicationRequest):
    data = request.dict()

    if data["application_id"] in applications:
        return {
            "message": "Duplicate request",
            "history": applications[data["application_id"]]
        }

    result = process_application(data)
    return result
