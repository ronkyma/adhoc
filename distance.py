from geopy.distance import geodesic

def calculate_distance(coord1, coord2):
    """
    Calculate the distance between two geographic coordinates using the Haversine formula.

    Parameters:
    coord1 (tuple): Latitude and longitude of the first point in decimal degrees.
    coord2 (tuple): Latitude and longitude of the second point in decimal degrees.

    Returns:
    float: The distance in kilometers.
    """
    distance = geodesic(coord1, coord2).kilometers
    return distance

if __name__ == "__main__":
    # Coordinates of two points (latitude, longitude) in decimal degrees
    coord1 = (34.0522, -118.2437)  # Los Angeles
    coord2 = (40.7128, -74.0060)   # New York

    distance = calculate_distance(coord1, coord2)
    print(f"Distance between Los Angeles and New York: {distance:.2f} km")
