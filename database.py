import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_db():
    conn = psycopg2.connect(
        host="localhost",
        database="ticket_system",
        user=os.getenv("USER"),
        cursor_factory=RealDictCursor
    )
    return conn