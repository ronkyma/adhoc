import geopandas as gpd
import matplotlib.pyplot as plt

# Load land use data from a GeoJSON file
file_path = 'landuse_data.geojson'
landuse_data = gpd.read_file(file_path)

# Display basic information about the dataset
print(landuse_data.head())

# Plot the land use data
landuse_data.plot(column='LandUseType', legend=True, figsize=(10, 8))
plt.title('Land Use Distribution')
plt.show()

# Perform spatial analysis or other data manipulations as needed
# Example: Calculate area for each land use type
landuse_area = landuse_data.groupby('LandUseType').area.sum()

# Plot the land use area distribution
landuse_area.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Land Use Area Distribution')
plt.xlabel('Land Use Type')
plt.ylabel('Area (square units)')
plt.show()
