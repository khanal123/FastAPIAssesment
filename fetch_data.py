import aiohttp
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import SessionLocal, Pokemon

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"

async def fetch_pokemon_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(POKEAPI_URL) as response:
            data = await response.json()
            return data['results']

async def store_pokemon_data(pokemon_data):
    async with SessionLocal() as db_session:
        for pokemon in pokemon_data:
            async with aiohttp.ClientSession() as session:
                async with session.get(pokemon['url']) as response:
                    details = await response.json()
                    new_pokemon = Pokemon(
                        name = details['name'],
                        image_url = details['sprites']['front_default'],
                        type = details['types'][0]['type']['name']
                    )
                    db_session.add(new_pokemon)
        await db_session.commit()

async def main():
    pokemon_data = await fetch_pokemon_data()
    await store_pokemon_data(pokemon_data)

if __name__ == "__main__":
    asyncio.run(main())
