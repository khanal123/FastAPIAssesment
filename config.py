import os

class Settings:
    POSTGRES_USER = os.getenv("POSTGRES_USER","postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","suman123")
    POSTGRES_DB = os.getenv("POSTGRES_DB","pokemondb")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST","localhost")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT","5432")
settings = Settings()