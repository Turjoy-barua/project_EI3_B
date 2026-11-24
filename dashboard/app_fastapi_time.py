from fastapi import APIRouter, FastAPI
from datetime import datetime

app = FastAPI()
router = APIRouter(prefix='/api')

@router.get("/get_time")
def get_time():
    return {"current_time": datetime.now().isoformat()}

app.include_router(router)