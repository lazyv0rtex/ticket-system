from pydantic import BaseModel
from typing import Literal

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    user_id: int
 
 
class TicketUpdate(BaseModel):
    title: str
    description: str
    priority: Literal["low", "medium", "high"]
    status: Literal["open", "closed"]