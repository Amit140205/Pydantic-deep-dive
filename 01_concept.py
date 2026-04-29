from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Inserted")

patient_info={"name": "Rahul", "age": 49}

patient1=Patient(**patient_info) # **=>used for unpacking the dictionary

insert_patient_data(patient1)