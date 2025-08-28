import geopandas as gpd
import matplotlib.pyplot as plt

world_map = gpd.read_file("ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp")

world_map.plot(edgecolor="orange")
plt.title("World Map with Country Borders")
plt.show()
