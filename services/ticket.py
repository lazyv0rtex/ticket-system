from sqlalchemy.orm import Session
from models.database_models import Ticket

def create_ticket(db: Session, ticket: dict):
    db_ticket = Ticket(
        title=ticket["title"],
        description=ticket["description"],
        priority=ticket["priority"],
        user_id=ticket["user_id"],
        status="open"
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket_data: dict):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db_ticket.title = ticket_data["title"]
        db_ticket.description = ticket_data["description"]
        db_ticket.priority = ticket_data["priority"]
        db_ticket.status = ticket_data["status"]
        db.commit()
        db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
        return True
    return False

def get_all_tickets(db: Session):
    return db.query(Ticket).all()
