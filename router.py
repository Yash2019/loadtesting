from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from scehema import Response
from database.db import get_db
from service.logic import get_result


router = APIRouter()

@router.get('/get_results{roll_number}', response_model=Response)
async def get_results_endpoint(roll_number: str, db: AsyncSession = Depends(get_db)):
    return await get_result(roll_number, db)
