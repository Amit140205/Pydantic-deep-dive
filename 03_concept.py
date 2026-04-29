from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 chars", examples=["Rahul", "Jhuma"])]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int=Field(ge=18, le=60)
    weight: float=Field(gt=0)
    height: Annotated[float, Field(gt=4, strict=True)]
    married: Annotated[bool, Field(default=False, description="Is the patient married or not")] # default value False
    allergies: Optional[List[str]]=None # mandatory to assign None if specified Optional[] 
    contact_details: Dict[str, str]

def insert_patient_info(patient_info: Patient):
    # print(patient_info.name)
    # print(patient_info.age)
    print(patient_info)
    print("Inserted")

patient_info={
    "name": "Rahul", 
    "email": "abc@gmail.com",
    "linkedIn_url": "https://linkedIn.com/1232",
    "age": 49,
    "weight": "80.09", # allow type-coercion
    "height": 5.6, # to stop type-coercion - use strict=True inside Field function
    # "married": False,
    # "allergies": ["dust"],
    "contact_details": {"email": "abc@mail.com", "phone": "2441139"}
}

patient1=Patient(**patient_info)

insert_patient_info(patient1)