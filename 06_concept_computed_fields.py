from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import List, Dict, Optional, Annotated

# here I have two fields 1. weight 2. height, now I want to calculate a new field name bmi at runtime using these two fields

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr 
    weight: float # kg
    height: float # meters
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact_details: Annotated[Dict[str, str], Field(default=None)]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2), 2)
        return bmi

patient_info={
    "name": "Rahul",
    "age": "60",
    "email": "abc@hdfc.com",
    "weight": 80.50,
    "height": 1.70,
    "married": False,
    "contact_details": {"emergency": "2441139"}
}

patient1=Patient(**patient_info)

print(patient1)