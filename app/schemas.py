from typing import List
from pydantic import BaseModel


class QuoteBase(BaseModel):
    pass

class Quote(QuoteBase):
    id: int
    author: str
    quote: str
    source: str
    year: str
    class Config:
        orm_mode = True


class QuoteBaseTrotsky(BaseModel):
    pass

class QuoteTrotsky(QuoteBase):
    id: int
    author: str
    quote: str
    source: str
    topic: str
    year: str
    class Config:
        orm_mode = True