import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Vehicle import Vehicle
from Recommendation.RecommendNearestVehicle import find_nearest_vehicle
from Recommendation.RecommendHighestBatteryVehicle import find_vehicle_with_highest_battery


# Example Vehicles
vehicles = np.array([
    Vehicle(101, 'CityA', 'CityB', 10, 75),
    Vehicle(102, 'CityB', 'CityC', 20, 60),
    Vehicle(103, 'CityA', 'CityD', 5, 90),
    Vehicle(104, 'CityC', 'CityE', 30, 50),
    Vehicle(105, 'CityD', 'CityA', 25, 85)
], dtype=object)

# Recommend vehicle closest to its destination
nearest_vehicle = find_nearest_vehicle(vehicles)
print("Vehicle closest to destination:", nearest_vehicle)

# Recommend vehicle with the highest battery level
highest_battery_vehicle = find_vehicle_with_highest_battery(vehicles)
print("Vehicle with the highest battery level:", highest_battery_vehicle)
