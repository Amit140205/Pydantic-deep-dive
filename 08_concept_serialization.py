from pydantic import BaseModel

# aim is to - convert pydantic model object to json/dict

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str="Male"
    age: int
    address: Address

address_dict={"city": "kolkata", "state": "south 24 parganas", "pin": "700042"}
address1=Address(**address_dict)

patient_dict={"name": "Rahul", "gender": "male", "age": 80, "address": address1}
patient1=Patient(**patient_dict)

print(patient1)

patient_convert_dict=patient1.model_dump()
print(type(patient_convert_dict))

patient_convert_json=patient1.model_dump_json()
print(type(patient_convert_json))

# another major advantage of using this is, we can control the model fields according to our need

# 1. include
temp1=patient1.model_dump(include=["name"])
print(temp1)

# 2. exclude
temp2=patient1.model_dump(exclude=["gender"])
print(temp2)
# or
temp3=patient1.model_dump(exclude={"address": ["pin"]}) # even applicable for nested models
print(temp3)

# or exclude_unset=> suppose I do not provide the gender value and set "Male" as default value, now in output I do not want to show gender because it is not provided
patient_new_dict={"name": "Rahul", "age": 80, "address": address1}
patient2=Patient(**patient_new_dict)
temp4=patient2.model_dump(exclude_unset=True)
print(temp4)