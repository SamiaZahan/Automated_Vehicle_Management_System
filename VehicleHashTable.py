import numpy as np

class VehicleHashTable:
    def __init__(self, size, road_network):
        self.size = size
        self.table = np.empty(size, dtype=object)  # Numpy array to store vehicles
        self.road_network = road_network  # The road network graph to check valid locations
        self.count = 0  # Keep track of the number of vehicles added

    def hash_function(self, vehicle_id):
        """Simple hash function based on the vehicle ID."""
        return vehicle_id % self.size

    def is_full(self):
        return self.count == self.size

    def insert_vehicle(self, vehicle):
        """Inserts a vehicle into the hash table using linear probing for collision resolution."""
        if self.is_full():
            print("Error: Hash table is full")
            return

        # Check if the source and destination exist in the road network
        if not self.road_network.find_vertex(vehicle.get_location()) or not self.road_network.find_vertex(vehicle.get_destination()):
            print(f"Error: Either {vehicle.get_location()} or {vehicle.get_destination()} doesn't exist in the road network.")
            return

        # Check if an edge exists between the current location and destination
        existing_edge_distance = self.road_network.get_edge_distance(vehicle.get_location(), vehicle.get_destination())
        if existing_edge_distance is None or existing_edge_distance != vehicle.get_distance_to_destination(): 
            # No edge exists, add a new edge
            self.road_network.add_edge(vehicle.get_location(), vehicle.get_destination(), vehicle.get_distance_to_destination())
    
        else:
            # Edge exists and has the same distance, no need to update
            print(f"Edge between {vehicle.get_location()} and {vehicle.get_destination()} already exists with the same distance. No update needed.")

        index = self.hash_function(vehicle.vehicle_id)
        original_index = index

        # Use linear probing for collision resolution
        while self.table[index] is not None:
            if self.table[index].vehicle_id == vehicle.vehicle_id:
                print(f"Error: Vehicle with ID {vehicle.vehicle_id} already exists.")
                return
            index = (index + 1) % self.size
            if index == original_index:
                print("Error: Hash table is full")
                return

        self.table[index] = vehicle
        self.count += 1
        print(f"Vehicle {vehicle.vehicle_id} inserted at index {index}")

    def search_vehicle(self, vehicle_id):
        """Searches for a vehicle by its ID using linear probing."""
        index = self.hash_function(vehicle_id)
        original_index = index

        while self.table[index] is not None:
            if self.table[index].vehicle_id == vehicle_id:
                return self.table[index]
            index = (index + 1) % self.size
            if index == original_index:
                break

        print(f"Vehicle with ID {vehicle_id} not found.")
        return None

    def delete_vehicle(self, vehicle_id):
        """Deletes a vehicle by its ID using linear probing to handle collision."""
        index = self.hash_function(vehicle_id)
        original_index = index

        while self.table[index] is not None:
            if self.table[index].vehicle_id == vehicle_id:
                print(f"Vehicle {vehicle_id} deleted from index {index}")
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size
            if index == original_index:
                break

        print(f"Vehicle with ID {vehicle_id} not found.")

    def display_vehicles(self):
        """Displays all vehicles in the hash table."""
        print("Vehicle Hash Table:")
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: Empty")
