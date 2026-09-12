# Ticket System API

A simple FastAPI help desk with PostgreSQL.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start PostgreSQL (already installed):
```bash
brew services start postgresql@15
```

3. Create database and table:
```bash
createdb ticket_system
python3 init_db.py
```

4. Run the app:
```bash
uvicorn main:app --reload
```

Visit: `http://localhost:8000/docs`

## API Endpoints

- `POST /tickets/` - Create ticket
- `GET /tickets/` - Get all tickets
- `GET /tickets/{id}` - Get one ticket
- `PUT /tickets/{id}` - Update ticket
- `DELETE /tickets/{id}` - Delete ticket
