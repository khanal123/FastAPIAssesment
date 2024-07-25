from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models import Pokemon, SessionLocal, init_db

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.get("/api/v1/pokemons")
async def get_pokemons(name: str = None , type: str = None, db: AsyncSession = Depends(get_db)):
    query = select(Pokemon)
    if name:
        query = query.where(Pokemon.name.ilike(f"%{name}%"))
    if type:
        query = query.where(Pokemon.type.ilike(f"%{type}%"))
    
    result = await db.execute(query)
    pokemons = result.scalars().all()
    return pokemons