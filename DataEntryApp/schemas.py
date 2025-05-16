from pydantic import BaseModel

class Schema_User(BaseModel):
    user: str

class Schema_Agent(BaseModel):
    agent: str

class Schema_Response(BaseModel):
    id: int
    agent: str