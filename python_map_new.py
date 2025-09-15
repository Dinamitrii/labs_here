import folium


def show_map():
    political_countries_url = (
        "https://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )

    mpc = folium.Map(location=(30, 10), zoom_start=9, tiles="cartodb positron")

    folium.GeoJson(political_countries_url).add_to(mpc)


    mpc = mpc._repr_html_()





    # m.save("footprint.html")





