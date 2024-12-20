from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.schemas import *
from app.database import get_db
from app.Models.create_models import Specialization, Group
router = APIRouter()

# Define your update endpoints here

@router.post("/api/v1/update_specialization")
async def update_specialization(item: UpdateSpecializationModel, db: Session = Depends(get_db)):
    try: 
        specialization = db.query(Specialization).filter(Specialization.id == item.id).first()
        if specialization is None:
            return JSONResponse(content={"message": "specialization not founded!"})
        specialization.name = item.name
        db.commit()
        return JSONResponse(content={"message": "specialization updated!"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)})
    
@router.post("/api/v1/update_group")
async def update_group(item: UpdateGroupModel, db: Session = Depends(get_db)):
    try:
        group = db.query(Group).filter(Group.id == item.id).first()
        if group is None:
            return JSONResponse(content={"message": "group not founded!"})
        group.name = item.name
        group.id_specialization = item.id_specialization
        db.commit()
        return JSONResponse(content={"message": "group updated!"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)})

@router.post()