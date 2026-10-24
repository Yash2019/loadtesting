from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from scehema import Response
from database.db import get_db
from fastapi import HTTPException, status
from service.logic import get_result


router = APIRouter()

@router.get('/get_results/{roll_number}', response_model=Response)
async def get_results_endpoint(roll_number: str, db: AsyncSession = Depends(get_db)):
    result =  await get_result(roll_number, db)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return result

