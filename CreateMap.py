import folium

def create_map(center, markers):
    """
    Create an interactive map with markers.
    
    Parameters:
        center (tuple): Latitude and longitude of the map's center in (latitude, longitude) format.
        markers (list): List of tuples containing latitude, longitude, and popup text for each marker.
        
    Returns:
        folium.Map: An interactive map object.
    """
    m = folium.Map(location=center, zoom_start=10)
    
    for marker in markers:
        lat, lon, popup_text = marker
        folium.Marker([lat, lon], popup=popup_text).add_to(m)
    
    return m

if __name__ == "__main__":
    # Center of the map (latitude, longitude)
    map_center = (37.7749, -122.4194)  # San Francisco, CA
    
    # List of markers: (latitude, longitude, popup text)
    markers = [
        (37.7749, -122.4194, "San Francisco, CA"),
        (34.0522, -118.2437, "Los Angeles, CA"),
        (41.8781, -87.6298, "Chicago, IL"),
        
        (29.7604, -95.3698, "Houston, TX")
    ]
    
    map_object = create_map(map_center, markers)
    map_object.save("interactive_map.html")
