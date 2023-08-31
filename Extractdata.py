import geopandas as gpd

# Path to the shapefile y23
# ou want to extract data from
shapefile_path = 'path/to/your/shapefile.shp'

# Read the shapefile using geopandas
gdf = gpd.read_file(shapefile_path)

# Display basic information about the GeoDataFrame
print("Number of features:", len(gdf))
print("Columns:", gdf.columns)
print("Coordinate Reference System (CRS):", gdf.crs)

# You can perform various operations with the extracted data
# For example, you can plot the data using the plot() function
gdf.plot()

# You can also access specific columns or perform spatial queries
# For instance, to select features that satisfy a condition
selected_features = gdf[gdf['population'] > 100000]

# To save the selected features to a new shapefile
output_path = 'path/to/output/selected_features.shp'
selected_features.to_file(output_path)

print("Selected features saved to:", output_path)
