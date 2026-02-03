import requests
from backend.config import OPENWEATHER_API_KEY

def search_city(query):

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={OPENWEATHER_API_KEY}"

    response = requests.get(url)
    data = response.json()

    results = []

    for item in data:
        results.append({
            "name": item["name"],
            "state": item.get("state", ""),
            "country": item["country"],
            "lat": item["lat"],
            "lon": item["lon"]
        })

    return results
