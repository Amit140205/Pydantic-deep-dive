from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import List, Dict, Optional, Annotated

# now aim is to validate multiple keys' values
# Suppose I want to check if age over 55 then contact_details must have emergency_no as key

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact_details: Annotated[Dict[str, str], Field(default=None)]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age>55 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 55, must have an emergency contact")
        
        return model

patient_info={
    "name": "Rahul",
    "age": "60",
    "email": "abc@hdfc.com",
    "weight": 80.50,
    "married": False,
    "contact_details": {"emergency": "2441139"}
}

patient1=Patient(**patient_info)

print(patient1)