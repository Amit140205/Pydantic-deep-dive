from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Now aim is to validate paticular key's value (single key-value)
# Suppose I want, email must have "hdfc.com" or "icici.com" at the end

class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact_details: Annotated[Optional[Dict[str, str]], Field(default=None)]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        domain=["hdfc.com", "icici.com"]
        domain_name=value.split("@")[-1]

        if domain_name not in domain:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator("name")
    @classmethod
    def name_transform(cls, value):
        # print(cls)
        return value.upper()
    
    # we can access value before and after(by default) type-coercion
    @field_validator("age", mode="after")
    @classmethod
    def age_validator(cls, value):
        if 18<=value<=60:
            return value
        raise ValueError("Age should be between 18 and 60")

patient_info={
    "name": "Rahul",
    # "age": 34, # here no issue because I pass age as int
    "age": "40", # problem arrives here because I pass age as string and access age value before type-coercion
    # "email": "abc@gmail.com", # do not work due to field validator,
    "email": "abc@hdfc.com",
    "weight": 80.50,
    "married": False
}

patient1=Patient(**patient_info)

print(patient1)