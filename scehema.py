from pydantic import BaseModel

class Response(BaseModel):
    roll_number: str
    name: str
    maths: int
    physics: int
    chemistry: int 
    total: int

class Recieve(BaseModel):
    roll_number: str