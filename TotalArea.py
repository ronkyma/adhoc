import geopandas as gpd
import matplotlib.pyplot as plt

# Load a shapefile (replace 'path/to/your/shapefile.shp' with your shapefile)
shapefile_path = 'path/to/your/shapefile.shp'
gdf = gpd.read_file(shapefile_path)

# Display the first few rows of the attribute data
print(gdf.head())

# Basic geospatial analysis
# Calculate the total area of all features
total_area = gdf['geometry'].area.sum()
print(f"Total area: {total_area} square units")

# Calculate summary statistics for a numeric attribute (e.g., population)
if 'population' in gdf.columns:
    max_population = gdf['population'].max()
    min_population = gdf['population'].min()
    print(f"Mean Population: {mean_population}")
    print(f"Max Population: {max_population}")
    print(f"Min Population: {min_population}")

# Visualize the shapefile
gdf.plot()
plt.title('GIS Data Visualization')
plt.show()
