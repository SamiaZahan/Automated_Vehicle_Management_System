import sys
import os
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from MyDataStructures.DSAHeap import DSAHeap

def heapsort_vehicles_by_distance(vehicle_table):
    """Sorts the vehicles by distance to destination using heapsort (ascending order)."""
    size = vehicle_table.count
    heap = DSAHeap(size)

    # Insert all non-None vehicles into the heap with distance as the priority
    for vehicle in vehicle_table.table:
        if vehicle is not None:
            heap.add(vehicle.get_distance_to_destination(), vehicle)

    # Perform heapsort and return sorted vehicles
    sorted_entries = heap.heapSort()  # Get sorted vehicles by distance
    sorted_vehicles = np.empty(size, dtype=object)

    for i in range(size):
        sorted_vehicles[i] = sorted_entries[i].getValue()

    return sorted_vehicles

def find_nearest_vehicle(vehicle_table):
    """Recommends the vehicle closest to its destination."""
    sorted_vehicles = heapsort_vehicles_by_distance(vehicle_table)
    return sorted_vehicles[0]  # Closest vehicle is at index 0 after ascending heapsort
