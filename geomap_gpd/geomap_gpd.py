import geopandas as gpd
import matplotlib.pyplot as plt

world_map = gpd.read_file("/home/dinamitrii/PycharmProjects/labs_here/geomap_gpd/ne_110m_admin_0_countries"
                          "/ne_110m_admin_0_countries.shp")

world_map.plot(edgecolor="purple", linewidth=1)
plt.title("World Map with Country Borders")
plt.show()
