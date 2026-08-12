from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.database.database import engine

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


async def get_db():
    async with SessionLocal() as db:
        yield db