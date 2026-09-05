from fastapi import FastAPI
    
from routers.tickets import router as tickets_router
from routers.health import router as health_router
    
app = FastAPI(
    title="Help Desk API",
    version="1.0.0"
)
    

app.include_router(tickets_router)
app.include_router(health_router)

