from MainRawData import *
from geopy.distance import geodesic


newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(geodesic(newport_ri, cleveland_oh).miles)


def addHubMarkers():
    for Hub, detail in CourierCompanies.items():
        folium.Marker(
            location=detail["location"],
            popup=f"<div style='width: max-content;text-align: center; font-weight: bold'>{detail['name']} - {Hub}</div>",
            tooltip=f"HUB - {Hub}",
            icon=folium.Icon(icon='truck', prefix='fa', color=detail['icon'])
        ).add_to(myMap)


def addCustomerMarkers():
    pass


def Door_to_Door_Distance():
    for customer, data in CustomerData.items():
        print(customer, f"--> Distance from {data['Origin']['name']} to {data['Destination']['name']} is", geodesic(data['Origin']['location'], data['Destination']['location']).kilometers, "Km")


addHubMarkers()
Door_to_Door_Distance()
auto_open_Map('HubsLocator.html')
