from pydantic import BaseModel, Field

class Post(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str
    body: str

    class Config:
        populate_by_name = True