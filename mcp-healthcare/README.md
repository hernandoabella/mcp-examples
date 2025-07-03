# MCP Healthcare App Tutorial
Build a Role-Based Healthcare App with Model-Context Protocol

This complete tutorial will guide you through building a secure, context-aware healthcare dashboard using:
- Streamlit (for an elegant frontend)
- MCP (Model-Context Protocol for dynamic data)
- Python + FastAPI (backend)

### 📂 Project Structure

```
mcp-healthcare/
├── backend/
│   ├── main.py          # FastAPI server
│   ├── models.py        # MCP-powered models
│   └── requirements.txt
└── frontend/
    ├── app.py           # Streamlit UI
    └── requirements.txt
```

## 1. Backend Setup (FastAPI)
#### backend/requirements.txt
```
fastapi==0.95.2
uvicorn==0.22.0
pydantic==2.0
python-multipart==0.0.6
```

### backend/models.py (MCP Core Logic)

```python
from enum import Enum
from pydantic import BaseModel

class UserRole(str, Enum):
    DOCTOR = "doctor"
    NURSE = "nurse"
    PATIENT = "patient"

class Patient(BaseModel):
    id: str
    name: str
    age: int
    conditions: list[str]
    medications: list[str]
    lab_results: dict
    
    def get_view(self, role: UserRole):
        # MCP: Context-Sensitive Data Filtering
        data = {"id": self.id, "name": self.name}
        
        if role == UserRole.DOCTOR:
            data.update({
                "conditions": self.conditions,
                "medications": self.medications,
                "lab_results": self.lab_results
            })
        elif role == UserRole.NURSE:
            data.update({
                "conditions": self.conditions,
                "medications": self.medications
            })
        elif role == UserRole.PATIENT:
            data["age"] = self.age
            
        return data
```

### backend/main.py (API Server)
```python
from fastapi import FastAPI, HTTPException
from models import Patient, UserRole

app = FastAPI()

# Sample Database
patients_db = {
    "P001": Patient(
        id="P001",
        name="John Doe",
        age=45,
        conditions=["Hypertension", "Type 2 Diabetes"],
        medications=["Metformin", "Lisinopril"],
        lab_results={"HbA1c": 6.5, "BP": "130/80"}
    )
}

@app.post("/patient/{patient_id}")
async def get_patient(patient_id: str, role: UserRole):
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient = patients_db[patient_id]
    return patient.get_view(role)
```

### Run the backend:
```bash
uvicorn main:app --reload
```
## 2. Streamlit Frontend
### frontend/requirements.txt

```
streamlit==1.25.0
requests==2.31.0
plotly==5.15.0
```

### frontend/app.py (Complete UI)

```python
import streamlit as st
import requests
import plotly.express as px

# Config
BACKEND_URL = "http://localhost:8000"
st.set_page_config(layout="wide")

# --- Session State ---
if "role" not in st.session_state:
    st.session_state.role = "doctor"

# --- Sidebar ---
with st.sidebar:
    st.title("⚕️ MCP Healthcare")
    role = st.radio(
        "Select Role:",
        ["Doctor", "Nurse", "Patient"],
        index=["Doctor", "Nurse", "Patient"].index(st.session_state.role)
    )
    st.session_state.role = role.lower()
    
    st.markdown("---")
    st.info("🔒 Model-Context Protocol ensures data security by role.")

# --- Main Dashboard ---
st.title(f"👨‍⚕️ {role} Dashboard")
patient_id = st.selectbox("Select Patient", ["P001"])

if st.button("Load Patient Data"):
    response = requests.post(
        f"{BACKEND_URL}/patient/{patient_id}",
        json={"role": st.session_state.role}
    )
    
    if response.status_code == 200:
        data = response.json()
        
        # --- Dynamic Display Based on Role ---
        cols = st.columns(2)
        
        with cols[0]:
            st.subheader("Patient Profile")
            st.json({
                "Name": data["name"],
                "Age": data.get("age", "N/A"),
                "ID": data["id"]
            })
        
        with cols[1]:
            if st.session_state.role == "doctor":
                st.subheader("Lab Results")
                fig = px.bar(
                    x=list(data["lab_results"].keys()),
                    y=list(data["lab_results"].values()),
                    title="Blood Test Results"
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # --- Conditionally Display Medical Info ---
        if "conditions" in data:
            with st.expander("Medical Details"):
                cols = st.columns(2)
                
                with cols[0]:
                    st.markdown("### Conditions")
                    for condition in data["conditions"]:
                        st.write(f"- {condition}")
                
                if "medications" in data:
                    with cols[1]:
                        st.markdown("### Medications")
                        for med in data["medications"]:
                            st.write(f"- 💊 {med}")
    else:
        st.error(f"Error: {response.text}")

# --- MCP Explanation ---
st.markdown("---")
st.subheader("How MCP Works")
st.image("https://i.imgur.com/xyz1234.png", caption="Model-Context Protocol Flow")  # Replace with your diagram
```

## 3. Key Streamlit UI Features
### 1. Role Switching

```python
role = st.radio("Select Role:", ["Doctor", "Nurse", "Patient"])
```

### 2. Dynamic Data Display

```python
if st.session_state.role == "doctor":
    st.plotly_chart(lab_results_chart)
```

### 3. Session State Management

```python
if "role" not in st.session_state:
    st.session_state.role = "doctor"
```
### 4. Visualizations

```python
fig = px.bar(x=lab_keys, y=lab_values)
st.plotly_chart(fig)
```

## 🚀 Running the App
### 1. Start the backend (in one terminal):

```bash
cd backend
uvicorn main:app --reload
```

### 2. Run Streamlit (in another terminal):

```bash
cd frontend
streamlit run app.py
```

## Why This Architecture Rocks?

### 1. MCP Ensures Security
- Data automatically filters by role
- No manual permission checks needed

### 2. Streamlit = Rapid Prototyping
- Build a polished UI in <100 lines
- Built-in caching (@st.cache_data)

### 3. FastAPI Backend
- Lightweight + async support
- Automatic OpenAPI docs
