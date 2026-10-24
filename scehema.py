from pydantic import BaseModel, ConfigDict

class Response(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    roll_number: str
    name: str
    maths: int
    physics: int
    chemistry: int 
    total: int

class Recieve(BaseModel):
    roll_number: str