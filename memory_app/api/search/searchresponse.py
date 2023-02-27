from pydantic import BaseModel
from datetime import datetime

class SearchResponse(BaseModel):
    firstname: str
    surname: str
    position: str
    date_of_birth: datetime = None
    description: str = None
