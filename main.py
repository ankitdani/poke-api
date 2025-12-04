from fastapi import FastAPI, Path, Query
import httpx

app = FastAPI()

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.get("/pokemons")
async def get_all_pokemon(
    limit: int = Query(20, gt = 0, lt = 1000),
    offset: int = Query(0, ge = 0, lt = 1000)
):
    
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={"limit": limit, "offset": offset})
        data = response.json()
        pokemon_names = [pokemon["name"] for pokemon in data["results"]]
        # pokemon_names = []
        # for pokemon in data["results"]:
        #     pokemon_names.append(pokemon["name"])

    return {"pokemon" : pokemon_names }

@app.get("/pokemon/{id}")
async def get_pokemon(id: int = Path(..., gt=0, lt=999, description="pokemon id must be greater than 0 and less than 999")):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}{id}")
        pokemon_detail = response.json()
    return {"details": pokemon_detail}
        
def main():
    print("Hello from pokeapi!")

if __name__ == "__main__":
    main()
