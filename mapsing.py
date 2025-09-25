# installing packages
import geocoder
import folium

# defining my function
def get_location(ip_address):
    location = geocoder.ip(ip_address)
    return location


# loading my ip_address
myip = '46.10.204.55'
location_info = get_location(myip)

print('country:', location_info.country)
print('city:', location_info.city)
print('latitude, longitude:', location_info.latlng[0], location_info.latlng[1])

# Creating a Folium map
coordinate = [location_info.latlng[0], location_info.latlng[1]]
myloc = folium.Map(location=coordinate, zoom_start=14, popup='My Location')

# Correcting the icon_color spelling
folium.Marker(coordinate, icon=folium.Icon(color='blue', icon_color='blue', prefix='fa', icon='male')).add_to(myloc)

# Adding a circle around the location
folium.Circle(location=coordinate, radius=100).add_to(myloc)

# Saving the map as an HTML file
myloc.save('my_mapsing.html')
