from pydantic import BaseModel
from typing import Literal

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
 
 
class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "closed"]