import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from RoadNetwork import RoadNetworkGraph
# Initialize the graph with a maximum number of 5 locations
road_network = RoadNetworkGraph()

# Create a numpy array for the locations
locations = np.array(['CityA', 'CityB', 'CityC', 'CityD', 'CityE', 'CityF'], dtype=object)

# Add locations to the graph
for i in range(locations.size):
    road_network.add_vertex(locations[i])

# Create a numpy array for the roads and distances
roads = np.array([
    ('CityA', 'CityB', 12),
    ('CityA', 'CityC', 7),
    ('CityB', 'CityD', 5),
    ('CityC', 'CityD', 10),
    ('CityD', 'CityE', 3),
    ('CityB', 'CityE', 15)
    
], dtype=object)

# Add roads (edges) to the graph
for i in range(roads.shape[0]):
    road_network.add_edge(roads[i][0], roads[i][1], roads[i][2])

# Display the graph structure
print("Graph as Adjacency List:")
road_network.display_graph()

# Retrieve and display neighbors for a specific location
print("\nNeighbors of CityA:")
neighbors_city_a = road_network.get_neighbors('CityA')
print(neighbors_city_a)

# Check if a path exists between two locations
print("\nPath Check:")
path_exists_a_to_f = road_network.is_path('CityA', 'CityF')
print("Path exists between CityA and CityF:", path_exists_a_to_f)

path_exists_b_to_c = road_network.is_path('CityB', 'CityC')
print("Path exists between CityB and CityC:", path_exists_b_to_c)
