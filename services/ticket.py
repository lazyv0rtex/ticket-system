from database import get_db
from test import Address

def create_ticket(ticket: dict):
    print("Creating ticket:", ticket)
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tickets (title, description, priority, status) VALUES (%s, %s, %s, %s) RETURNING *",
        (ticket["title"], ticket["description"], ticket["priority"], "open")
    )
    new_ticket = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return dict(new_ticket)

def get_ticket(ticket_id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets WHERE id = %s", (ticket_id,))
    ticket = cur.fetchone()
    cur.close()
    conn.close()
    return dict(ticket) if ticket else None

def update_ticket(ticket_id: int, ticket_data: dict):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tickets SET title = %s, description = %s, priority = %s, status = %s WHERE id = %s RETURNING *",
        (ticket_data["title"], ticket_data["description"], ticket_data["priority"], ticket_data["status"], ticket_id)
    )
    updated_ticket = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return dict(updated_ticket) if updated_ticket else None

def delete_ticket(ticket_id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tickets WHERE id = %s", (ticket_id,))
    deleted = cur.rowcount > 0
    conn.commit()
    cur.close()
    conn.close()
    return deleted

def get_all_tickets():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tickets")
    tickets = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(ticket) for ticket in tickets]


