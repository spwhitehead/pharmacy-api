import json

from fastapi import FastAPI

from models import Patient


app = FastAPI()


with open("patients.json", "r") as f:
    patient_list = json.load(f)

patients: list[Patient] = []

for patient in patient_list:
    patients.append(Patient(**patient))

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"


@app.get("/patients")
async def list_patients() -> list[Patient]:
    return patients


@app.post("/patients")
async def add_patient(patient: Patient) -> None:
    patients.append(patient)
    return "Patient added successfully"


@app.put("/patients/{first_name}")
async def update_patient(first_name: str, updated_patient: Patient) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients[i] = updated_patient
            return "Patient updated successfully"
        else:
            patients.append(updated_patient)
            return "Patient not found, created successfully"


@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name == first_name:
            patients.pop(i)
            return "Patient deleted successfully"
    return "Patient not found"
