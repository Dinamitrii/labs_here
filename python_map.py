# import folium package and create map
import folium


def generate_geo_map():
    generated_map = folium.Map(location=[42.6975, 23.3242], zoom_start=12)

    # Pass a string in popup parameter
    folium.Marker([42.6975, 23.3242], popup='https://predictorian.online').add_to(generated_map)

    generated_map.save("generated_map.html")

generate_geo_map()