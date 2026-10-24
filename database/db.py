from config import Config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)

Sessionlocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass


async def get_db():
    async with Sessionlocal() as db:
        yield db

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

