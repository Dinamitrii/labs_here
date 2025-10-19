from geopy.geocoders import Nominatim


geolocator = Nominatim(timeout=10, user_agent="Dinamitrii")

loc = "Dianabad bl 42 sofia 1172"

location = geolocator.geocode(loc)

print(location.address)
print((location.latitude, location.longitude))
