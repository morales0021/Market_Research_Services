from pydantic import BaseModel

class References(BaseModel):
    title: str
    link: str

class TextContentRefs(BaseModel):
    content: str
    references: list[References]