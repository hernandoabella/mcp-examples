EHR_DB = {
    "patient_001": {
        "name": "Alice Johnson",
        "age": 58,
        "conditions": ["hypertension", "type 2 diabetes"],
        "medications": ["metformin", "lisinopril"]
    },
    "patient_002": {
        "name": "Mark Lee",
        "age": 45,
        "conditions": ["asthma"],
        "medications": ["albuterol"]
    }
}

def get_patient_by_id(patient_id: str):
    return EHR_DB.get(patient_id)

async def query_medical_guidelines(condition: str) -> str:
    guidelines = {
        "hypertension": "Recommend low-sodium diet and ACE inhibitors.",
        "type 2 diabetes": "Suggest metformin and regular HbA1c monitoring.",
        "asthma": "Use inhaled corticosteroids and monitor peak flow."
    }
    return guidelines.get(condition, "No guideline found.")
