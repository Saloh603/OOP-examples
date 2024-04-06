import geocoder


def address_to_coordinates_osm(address):
    # Attempt to geocode using OpenStreetMap/Nominatim
    g = geocoder.osm(address)

    # Check if we got a valid response
    if g.ok:
        return g.latlng
    else:
        return None


# Full address
address = "Узбекистан, Ташкент, Юнусабадский, ул.Халка Автомобил Йули"

# Attempt to convert the address to coordinates
coordinates = address_to_coordinates_osm(address)

print("Coordinates:", coordinates)
