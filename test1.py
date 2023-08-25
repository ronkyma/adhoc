import requests

def get_geoinfo(location_name):
    username = "ronkyma"
    base_url = f"http://api.geonames.org/searchJSON?q={location_name}&maxRows=1&username={username}"

    response = requests.get(base_url)
    data = response.json()

    if "geonames" in data and data["geonames"]:
        result = data["geonames"][0]
        country = result["countryName"]
        population = result["population"]
        lat = result["lat"]
        lon = result["lng"]

        print(f"Location: {location_name}")
        print(f"Country: {country}")
        print(f"Population: {population}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
    else:
        print("Location not found.")

if __name__ == "__main__":
    location_name = input("Enter a location name: ")
    get_geoinfo(location_name)
