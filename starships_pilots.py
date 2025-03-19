import requests
import sys
import json

BASE_URL = "https://swapi.dev/api/films/"

def get_film_data(film_title):
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print("Error fetching films from SWAPI")
        return None

    films = response.json().get("results", [])
    for film in films:
        if film["title"].lower() == film_title.lower():
            return film
    return None

def get_starships_and_pilots(film):
    starships_info = []
    
    for starship_url in film["starships"]:
        starship_data = requests.get(starship_url).json()
        pilots = []
        
        for pilot_url in starship_data.get("pilots", []):
            pilot_data = requests.get(pilot_url).json()
            pilots.append(pilot_data.get("name", "Unknown"))
        
        starships_info.append({
            "starship": starship_data.get("name", "Unknown"),
            "pilots": pilots
        })

    return starships_info

def main():
    if len(sys.argv) != 2:
        print("Usage: python starships_pilots.py '<film_title>'")
        sys.exit(1)

    film_title = sys.argv[1]
    film = get_film_data(film_title)

    if not film:
        print(f"Film '{film_title}' not found.")
        sys.exit(1)

    result = {
        "film": film_title,
        "starships": get_starships_and_pilots(film)
    }

    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
