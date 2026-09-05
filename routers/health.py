from fastapi import APIRouter
    
    
router = APIRouter(
    tags=["Health"]
)

@router.get("/")
def get_health():
    return {"status": "ok"}
