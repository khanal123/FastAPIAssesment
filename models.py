from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_async_engine(DATABASE_URL, echo = True)
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine, class_=AsyncSession)

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Pokemon(Base):

    __tablename__ = "pokemons"

    id = Column(Integer,primary_key= True, index= True)
    name = Column(String, index= True)
    image_url = Column(String)
    type = Column(String)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)