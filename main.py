import json


with open("patients.json", "r") as f:
    patient_list = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"
