from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id:int
    name:str
    address:str

users:List[User]=[]
