from fastapi import FastAPI
from app.ehr import get_patient_by_id, query_medical_guidelines
from app.mcp_schemas import MCPRequest, MCPResponse
import uuid

app = FastAPI()

@app.post("/mcp/clinical-advice")
async def clinical_advice(request: MCPRequest):
    patient = get_patient_by_id(request.patient_id)
    if not patient:
        return MCPResponse(request_id=request.request_id, result={"error": "Patient not found."})

    advice = {}
    for condition in patient["conditions"]:
        guideline = await query_medical_guidelines(condition)
        advice[condition] = guideline

    log_id = str(uuid.uuid4())
    return MCPResponse(
        request_id=request.request_id,
        result={
            "patient": patient["name"],
            "advice": advice,
            "log_id": log_id
        }
    )
