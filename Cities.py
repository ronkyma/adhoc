import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import folium

# Load GIS data from a GeoJSON file
file_path = 'cities_data.geojson'
cities_data = gpd.read_file(file_path)

# Display basic information about the dataset
print(cities_data.head())

# Plot the GIS data with population-based color-coding
fig, ax = plt.subplots(figsize=(10, 8))
cities_data.plot(column='Population', cmap='YlGnBu', legend=True, ax=ax)
plt.title('Cities Population Distribution')
plt.show()

# Spatial analysis: Buffer around cities
buffer_distance = 0.1  # Buffer distance in degrees
cities_data['Buffer'] = cities_data.buffer(buffer_distance)

# Plot original and buffered data
fig, ax = plt.subplots(figsize=(12, 8))

cities_data.plot(ax=ax, color='lightgray', edgecolor='black', alpha=0.7)
cities_data.boundary.plot(ax=ax, color='black', linewidth=1)

cities_data['Buffer'].plot(ax=ax, color='orange', alpha=0.3)

plt.title('Buffered Area around Cities')
plt.show()

# Interactive map using Folium
m = folium.Map(location=[cities_data['geometry'].centroid.y.mean(), 
                         cities_data['geometry'].centroid.x.mean()], zoom_start=4)

# Add city markers with popups
for idx, row in cities_data.iterrows():
    folium.Marker([row['geometry'].y, row['geometry'].x], 
                  popup=f"{row['City']} - Population: {row['Population']}").add_to(m)

# Add buffered areas
for idx, row in cities_data.iterrows():
    folium.GeoJson(row['Buffer'].__geo_interface__,
                   style_function=lambda x: {'color': 'red', 'fillColor': 'orange', 'fillOpacity': 0.3}).add_to(m)

# Save the map as an HTML file
m.save('interactive_map.html')
