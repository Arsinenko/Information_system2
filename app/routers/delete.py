from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from app.Models.create_models import *
from app.database import get_db
from app.schemas.schemas import DeleteByIdModel

router = APIRouter()

@router.delete("/api/v1/delete_specialization/")
def delete_specialization(model: DeleteByIdModel, db: Session = Depends(get_db)):
    try: 
        specialization = db.query(Specialization).filter(Specialization.id == model.id).first()
        if not specialization:
            return JSONResponse(content={"message": "Specialization not found"}, status_code=404)
            
        db.delete(specialization)
        db.commit()
        return JSONResponse(content={"message": "Specialization deleted successfully"}, status_code=200)
    except Exception as e:
        db.rollback()
        return JSONResponse(content={"message": f"Error deleting specialization: {e}"}, status_code=500)
