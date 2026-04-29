from pydantic import BaseModel

# here in the Patient class, there is a field - address that depends upon another class "Address"
# Benefit: 
# 1. Better organization
# 2. Readability
# 3. Reusability
# 4. Validation

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict={"city": "kolkata", "state": "south 24 parganas", "pin": "700042"}
address1=Address(**address_dict)

patient_dict={"name": "Rahul", "gender": "male", "age": 80, "address": address1}
patient1=Patient(**patient_dict)

print(patient1)