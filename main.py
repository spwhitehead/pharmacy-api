import json

from fastapi import FastAPI

from models import Patient


app = FastAPI()


with open("patients.json", "r") as f:
    patient_list = json.load(f)

patients = list[Patient] = []

for person in patient_list:
    patients.append(Patient(**person))

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"
