from sqlalchemy.ext.asyncio import AsyncSession
from models.model import Student
from sqlalchemy import select


async def get_result(roll_number: str, db: AsyncSession):
    stmt = select(Student).where(
        Student.roll_number == roll_number
    )

    data = await db.execute(stmt)
    result = data.scalar_one_or_none()

    return result

