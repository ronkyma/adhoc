import geopandas as gpd
import matplotlib.pyplot as plt

# URL to a shapefile containing country boundaries (Natural Earth dataset)
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"

# Read the shapefile using geopandas
gdf_countries = gpd.read_file(url)

# Display basic information about the GeoDataFrame
print("Number of features:", len(gdf_countries))
print("Columns:", gdf_countries.columns)
print("Coordinate Reference System (CRS):", gdf_countries.crs)


# Plot the countries
gdf_countries.plot()
plt.title("World Countries")
plt.show()