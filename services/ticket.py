from database import db
from bson import ObjectId

collection = db["tickets"]

def create_ticket(ticket: dict):
    ticket["status"] = "open"
    result = collection.insert_one(ticket)
    ticket["_id"] = str(result.inserted_id)
    return ticket

def get_ticket(ticket_id: str):
    ticket = collection.find_one({"_id": ObjectId(ticket_id)})
    if ticket:
        ticket["_id"] = str(ticket["_id"])
    return ticket

def update_ticket(ticket_id: str, ticket_data: dict):
    collection.update_one({"_id": ObjectId(ticket_id)}, {"$set": ticket_data})
    return get_ticket(ticket_id)

def delete_ticket(ticket_id: str):
    result = collection.delete_one({"_id": ObjectId(ticket_id)})
    return result.deleted_count > 0

def get_all_tickets():
    tickets = list(collection.find())
    for ticket in tickets:
        ticket["_id"] = str(ticket["_id"])
    return tickets


