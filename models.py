from pydantic import BaseModel


class Patient(BaseModel):
    f_name: str
    l_name: str
    address: str
    age: int
