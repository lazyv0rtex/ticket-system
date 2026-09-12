from database import get_db

conn = get_db()
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        priority VARCHAR(50) NOT NULL,
        status VARCHAR(50) DEFAULT 'open'
    )
""")

conn.commit()
cur.close()
conn.close()

print("Database table created!")
