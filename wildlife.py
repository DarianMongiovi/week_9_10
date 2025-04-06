import geopandas as gpd
import matplotlib.pyplot as plt


url_wildlife_areas = "https://services1.arcgis.com/RbMX0mRVOFNTdLzd/arcgis/rest/services/MaineDIFW_WildlifeManagementAreas/FeatureServer/0/query?where=1%3D1&outFields=*&f=geojson"
gdf_wildlife_areas = gpd.read_file(url_wildlife_areas)

path_state_boundaries = r"/week_9_10/Maine.kml"
path_county_boundaries = r"/week_9_10/cb_2023_23_cousub_500k.kml"

gdf_states = gpd.read_file(path_state_boundaries)
gdf_counties = gpd.read_file(path_county_boundaries)

ax = gdf_wildlife_areas.plot(figsize=(10, 10), color='lightgreen', edgecolor='black', alpha=0.7)

gdf_states.plot(ax=ax, color='none', edgecolor='blue', linewidth=2)
gdf_counties.plot(ax=ax, color='none', edgecolor='gray', linewidth=0.5)

plt.title("Wildlife Management Areas in Maine with State and County Boundaries")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()
