def quicksort_vehicles_by_battery(vehicles, low, high):
    """Sorts the vehicles by battery level using quicksort (descending order)."""
    if low < high:
        pivot_index = partition(vehicles, low, high)
        quicksort_vehicles_by_battery(vehicles, low, pivot_index - 1)
        quicksort_vehicles_by_battery(vehicles, pivot_index + 1, high)

def partition(vehicles, low, high):
    """Partition the array around the pivot for quicksort."""
    pivot = vehicles[high].get_battery_level()
    i = low - 1
    for j in range(low, high):
        if vehicles[j].get_battery_level() > pivot:  # Descending order
            i += 1
            vehicles[i], vehicles[j] = vehicles[j], vehicles[i]
    vehicles[i + 1], vehicles[high] = vehicles[high], vehicles[i + 1]
    return i + 1

def find_vehicle_with_highest_battery(vehicle_table):
    """Recommends the vehicle with the highest battery level."""
    # Filter out None entries to create a list of valid vehicles
    valid_vehicles = [vehicle for vehicle in vehicle_table.table if vehicle is not None]
    
    # Apply quicksort to the valid vehicles list
    quicksort_vehicles_by_battery(valid_vehicles, 0, len(valid_vehicles) - 1)
    
    # Return the vehicle with the highest battery level (first after descending sort)
    return valid_vehicles[0]  # Vehicle with highest battery is at index 0 after descending quicksort
