# Ticket System API

A simple FastAPI help desk with MongoDB.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install and start MongoDB:
```bash
# macOS
brew install mongodb-community
brew services start mongodb-community
```

3. Run the app:
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
