import asyncio
import asyncpg

from config import Config
from database.db import create_table
from models.model import Student


async def load_students():
    await create_table()

    database_url = Config.DATABASE_URL.replace(
        "postgresql+asyncpg://",
        "postgresql://",
        1,
    )

    connection = await asyncpg.connect(database_url)

    try:
        with open('results.csv', 'rb') as csv_file:
            await connection.copy_to_table(
                'students',
                source=csv_file,
                format='csv',
                header=True,
                columns=[
                    'roll_number',
                    'name',
                    'maths',
                    'physics',
                    'chemistry',
                    'total',
                ],
            )

    finally:
        await connection.close()

if __name__ == "__main__":
    asyncio.run(load_students())