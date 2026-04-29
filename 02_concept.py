from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

def insert_patient_info(patient_info: Patient):
    # print(patient_info.name)
    # print(patient_info.age)
    print(patient_info)
    print("Inserted")

patient_info={
    "name": "Rahul", 
    "age": 49,
    "weight": 80.09,
    "married": False,
    "allergies": ["dust"],
    "contact_details": {"email": "abc@mail.com", "phone": "2441139"}
}

patient1=Patient(**patient_info)

insert_patient_info(patient1)