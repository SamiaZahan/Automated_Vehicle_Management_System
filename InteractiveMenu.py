import numpy as np
from RoadNetwork import RoadNetworkGraph
from Vehicle import Vehicle
from VehicleHashTable import VehicleHashTable  # Import VehicleHashTable class
from Recommendation.RecommendNearestVehicle import *
from Recommendation.RecommendHighestBatteryVehicle import *

class InteractiveMenu:
    def __init__(self):
        # Initialize empty road network and vehicle hash table
        self.road_network = RoadNetworkGraph()  # Road network
        self.vehicle_table = VehicleHashTable(size=10, road_network=self.road_network)  # Hash table to store vehicles

    def display_menu(self):
        print("\n--- Vehicle Management System Menu ---")
        print("1. Add a Location to Road Network")
        print("2. Add a Road between Locations")
        print("3. Retrieve Neighbors of a Location")
        print("4. Check Path Existence Between Locations")
        print("5. Display Road Network")
        print("6. Add a Vehicle")
        print("7. Delete a Vehicle")
        print("8. Search for a Vehicle")
        print("9. Display All Vehicles")
        print("10. Sort Vehicles by Distance to Destination (Heapsort)")
        print("11. Sort Vehicles by Battery Level (Quicksort)")
        print("12. Recommend Vehicle Closest to Destination")
        print("13. Recommend Vehicle with Highest Battery Level")
        print("14. Exit")

    ### Road Network Operations ###
    def add_location(self):
        location = input("Enter location (e.g., CityA): ")
        if self.road_network.find_vertex(location) is not None:
            print(f"Error: Location {location} already exists in the road network.")
        else:
            self.road_network.add_vertex(location)
            print(f"Location {location} added successfully.")

    def add_road(self):
        location1 = input("Enter first location: ")
        location2 = input("Enter second location: ")
        try:
            distance = float(input("Enter distance between locations: "))
            if self.road_network.find_vertex(location1) and self.road_network.find_vertex(location2):
                self.road_network.add_edge(location1, location2, distance)
                # print(f"Road added between {location1} and {location2} with distance {distance}.")
            else:
                print(f"Error: One or both locations ({location1}, {location2}) do not exist in the road network.")
        except ValueError:
            print("Error: Invalid distance input. Please enter a valid number.")

    def retrieve_neighbors(self):
        location = input("Enter location to retrieve neighbors: ")
        neighbors = self.road_network.get_neighbors(location)
        if neighbors:
            print(f"Neighbors of {location}: {neighbors}")
        else:
            print(f"No neighbors found or {location} does not exist.")

    def check_path_existence(self):
        location1 = input("Enter source location: ")
        location2 = input("Enter destination location: ")
        if self.road_network.is_path(location1, location2):
            print(f"A path exists between {location1} and {location2}.")
        else:
            print(f"No path exists between {location1} and {location2}.")

    def display_road_network(self):
        print("\n--- Road Network ---")
        self.road_network.display_graph()

    ### Vehicle Operations using VehicleHashTable ###
    def add_vehicle(self):
        try:
            vehicle_id = int(input("Enter Vehicle ID: "))
            location = input("Enter Vehicle Location: ")
            destination = input("Enter Vehicle Destination: ")
            distance = float(input("Enter Distance to Destination: "))
            battery_level = float(input("Enter Battery Level: "))
            
            # Ensure both location and destination exist in the road network
            if self.road_network.find_vertex(location) and self.road_network.find_vertex(destination):
                new_vehicle = Vehicle(vehicle_id, location, destination, distance, battery_level)
                self.vehicle_table.insert_vehicle(new_vehicle)  # Use hash table to insert vehicle
            else:
                print(f"Error: One or both locations ({location}, {destination}) do not exist in the road network.")
        except ValueError as ve:
            print(f"Error: Invalid input. Please try again. {ve}")

    def delete_vehicle(self):
        try:
            vehicle_id = int(input("Enter Vehicle ID to delete: "))
            self.vehicle_table.delete_vehicle(vehicle_id)  # Use hash table to delete vehicle
        except ValueError:
            print("Error: Invalid input. Please enter a valid vehicle ID.")

    def search_vehicle(self):
        try:
            vehicle_id = int(input("Enter Vehicle ID to search: "))
            vehicle = self.vehicle_table.search_vehicle(vehicle_id)  # Use hash table to search for vehicle
            if vehicle:
                print(f"Vehicle found: {vehicle}")
            else:
                print(f"Vehicle with ID {vehicle_id} not found.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid vehicle ID.")

    def display_vehicles(self):
        self.vehicle_table.display_vehicles()

    def sort_vehicles_by_distance(self):
        if self.vehicle_table.count == 0:  # Check count instead of len()
            print("No vehicles available to sort.")
        else:
            sorted_vehicles = heapsort_vehicles_by_distance(self.vehicle_table)  # Pass the table to sorting function
            print("Vehicles sorted by distance to destination (ascending order):")
            for vehicle in sorted_vehicles:
                print(vehicle)

    def sort_vehicles_by_battery(self):
        if self.vehicle_table.count == 0:  # Check if there are any vehicles
            print("No vehicles available to sort.")
        else:
            # Extract only non-None vehicles from the hash table
            valid_vehicles = [vehicle for vehicle in self.vehicle_table.table if vehicle is not None]
            
            # Sort the valid vehicles by battery level in descending order
            quicksort_vehicles_by_battery(valid_vehicles, 0, len(valid_vehicles) - 1)
            
            # Display the sorted vehicles
            print("Vehicles sorted by battery level (descending order):")
            for vehicle in valid_vehicles:
                print(vehicle)

    def recommend_nearest_vehicle(self):
        if self.vehicle_table.count == 0:  # Check count instead of len()
            print("No vehicles available for recommendation.")
        else:
            nearest_vehicle = find_nearest_vehicle(self.vehicle_table)
            print("Recommended Vehicle Closest to Destination:")
            print(nearest_vehicle)

    def recommend_highest_battery_vehicle(self):
        if self.vehicle_table.count == 0:  # Check count instead of len()
            print("No vehicles available for recommendation.")
        else:
            highest_battery_vehicle = find_vehicle_with_highest_battery(self.vehicle_table)
            print("Recommended Vehicle with Highest Battery Level:")
            print(highest_battery_vehicle)

    ### Run Interactive Menu ###
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-14): ")

            if choice == '1':
                self.add_location()
            elif choice == '2':
                self.add_road()
            elif choice == '3':
                self.retrieve_neighbors()
            elif choice == '4':
                self.check_path_existence()
            elif choice == '5':
                self.display_road_network()
            elif choice == '6':
                self.add_vehicle()
            elif choice == '7':
                self.delete_vehicle()
            elif choice == '8':
                self.search_vehicle()
            elif choice == '9':
                self.display_vehicles()
            elif choice == '10':
                self.sort_vehicles_by_distance()
            elif choice == '11':
                self.sort_vehicles_by_battery()
            elif choice == '12':
                self.recommend_nearest_vehicle()
            elif choice == '13':
                self.recommend_highest_battery_vehicle()
            elif choice == '14':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 14.")

# Example usage
if __name__ == "__main__":
    menu = InteractiveMenu()
    menu.run()
