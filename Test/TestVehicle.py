import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RoadNetwork import RoadNetworkGraph
from VehicleHashTable import VehicleHashTable
from Vehicle import Vehicle
# Create a road network graph
road_network = RoadNetworkGraph()

# Add some locations (nodes) to the road network
road_network.add_vertex('CityA')
road_network.add_vertex('CityB')
road_network.add_vertex('CityC')
# road_network.add_vertex('CityD')
road_network.add_edge('CityA', 'CityB', 12)
road_network.add_edge('CityB', 'CityC', 15)

# Create a vehicle hash table
vehicle_table = VehicleHashTable(10, road_network)

# Create and insert vehicles into the hash table
vehicle1 = Vehicle(101, 'CityA', 'CityB', 12, 80)
vehicle2 = Vehicle(102, 'CityB', 'CityC', 15, 60)
vehicle3 = Vehicle(103, 'CityA', 'CityD', 25, 70)  # This should fail as 'CityD' doesn't exist in the road network

vehicle_table.insert_vehicle(vehicle1)  # Success
vehicle_table.insert_vehicle(vehicle2)  # Success
vehicle_table.insert_vehicle(vehicle3)  # Error, CityD doesn't exist in the road network

# Search for a vehicle
searched_vehicle = vehicle_table.search_vehicle(101)
if searched_vehicle:
    print(f"Found Vehicle: {searched_vehicle}")

# Display all vehicles
vehicle_table.display_vehicles()

# Delete a vehicle
vehicle_table.delete_vehicle(102)
vehicle_table.display_vehicles()
