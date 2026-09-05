from fastapi import APIRouter
    
from models.ticket import TicketCreate, TicketUpdate
from services.ticket import (
    create_ticket,
    get_ticket,
    update_ticket,
    delete_ticket,
    get_all_tickets
)
    
    
router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.get("/")
def get_tickets():
    return get_all_tickets()

@router.get("/{ticket_id}")
def get_ticket_by_id(ticket_id: str):
    return get_ticket(ticket_id)

@router.post("/")
def create_ticket_endpoint(ticket: TicketCreate):
    return create_ticket(ticket.model_dump())

@router.put("/{ticket_id}")
def update_ticket_endpoint(ticket_id: str, ticket: TicketUpdate):
    return update_ticket(ticket_id, ticket.model_dump())

@router.delete("/{ticket_id}")
def delete_ticket_endpoint(ticket_id: str):
    return delete_ticket(ticket_id)
