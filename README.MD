#POKEMON API

This is a FASTAPI-based API that retrieves Pokemondata from the PokeAPI, stores it in a PostgreSQL database,and serves it with filtering capabilities.

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```sh
   git clone 
   cd pokemon-api
   ```


2. Create a virtual environment and activate it.
   ```sh
   python -m venv venv
   source venv/Scripts/activate # On mac use source venv/bin/activate
   ```


3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```


4. Setup environment variables for the database configuration:
   ```sh
   export POSTGRES_USER =your_user
   export POSTGRES_PASSWORD =your_password
   export POSTGRES_DB =your_db
   export POSTGRES_HOST =localhost
   export POSTGRES_PORT =5432
   ```

### Fetch and Store Pokemon data

Run the script to fetch the data from the pokeAPI and store it in the PostgreSQL database:
```sh
python fetch_data.py
```
Start the API

Run the FastAPI application:
```sh
uvicorn main:app --reload
```
This API will be available at `http://127.0.0.1:8000/api/v1/pokemons`

Usage:

  - To get a list of all Pokemons:
    ```bash
    GET /api/v1/pokemons
    ```

  - To filter Pokemon by name:
    ```bash
    GET /api/v1/pokemons?name=pikachu
    ```

  - To filter Pokemon by type:
    ```bash
    GET /api/v1/pokemons?type=electric
    ```

  - To filter Pokemon by name and type 
    ```bash
    GET /api/v1/pokemons?name=pikachu&type=electric



