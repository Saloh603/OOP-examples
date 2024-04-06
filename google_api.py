from geopy.geocoders import Nominatim
import time
def get_coordinates(address):
    geolocator = Nominatim(user_agent="user")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude) if location else (None, None)


#open my json file and read it
import json
with open('fuel-stations.json', encoding='utf-8') as f:
  data = json.load(f)
  # print(data)

index = 0
while index < len(data):
  try:
    i = data[index]
    full_address = f'{i["address"]["country"]}, {i["address"]["city"]}, {i["address"]["district"]}, {i["address"]["street"]}'
    print(full_address)
    longitude, latitude = get_coordinates(full_address)
    print(longitude, latitude)
    i["address"]["longitude"] = longitude
    i["address"]["latitude"] = latitude
    print(i["address"])
    index += 1
    print(f">>>>>>>>>>>>>>>>{index}<<<<<<<<<<<<<<<<<<<<<<<<")
    time.sleep(1)  # Be mindful of the usage limits of the Nominatim API
  except Exception as e:
    print(f"Error: {e}")
    time.sleep(1)  # Adding a delay before retrying can help if the error is due to rate limits


with open('updated-fuel-stations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# print(get_coordinates("Узбекистан, Ташкент, Юнусабадский, ул. Тошкент"))