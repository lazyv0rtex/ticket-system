from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
    
from models.ticket import TicketCreate, TicketUpdate
from models.database_models import User
from database import get_db
from auth import get_current_user
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
def get_tickets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_tickets(db)

@router.get("/{ticket_id}")
def get_ticket_by_id(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_ticket(db, ticket_id)

@router.post("/")
def create_ticket_endpoint(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_ticket(db, ticket.model_dump(), current_user.id)

@router.put("/{ticket_id}")
def update_ticket_endpoint(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_ticket(db, ticket_id, ticket.model_dump())

@router.delete("/{ticket_id}")
def delete_ticket_endpoint(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_ticket(db, ticket_id)
