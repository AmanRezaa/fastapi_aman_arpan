from pydantic import BaseModel

class Blog(BaseModel):
    title : str
    content : str
    author : str
    created_at : str

