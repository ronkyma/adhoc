import geopandas as gpd
from shapely.geometry import Point

# Create a sample GeoDataFrame with points
data = {'ID': [1, 2, 3],
        'Latitude': [34.0522, 40.7128, 41.8781],
        'Longitude': [-118.2437, -74.0060, -87.6298]}

geometry = [Point(xy) for xy in zip(data['Longitude'], data['Latitude'])]
gdf = gpd.GeoDataFrame(data, geometry=geometry, crs='EPSG:4326')

# Define the buffer distance in degrees (you might need to adjust this based on your data)
buffer_distance_degrees = 1.0

# Create a buffer around the points

buffered_gdf['geometry'] = buffered_gdf.buffer(buffer_distance_degrees)

# Save the buffered GeoDataFrame to a file (e.g., shapefile or GeoJSON)
output_file = 'buffered_points.shp'
buffered_gdf.to_file(output_file)

print("Buffered GeoDataFrame saved to", output_file)
