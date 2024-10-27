import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyDataStructures.DSALinkedList import DSALinkedList
from MyDataStructures.DSAQueue import DSAQueue

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.adjacency_list = DSALinkedList()  # Linked list to store adjacent nodes and their distances
        self.visited = False  # Track if the node has been visited for path-checking algorithms

    def add_edge(self, neighbor, distance):
        self.adjacency_list.insert_last((neighbor, distance))

class RoadNetworkGraph:
    def __init__(self):
        self.vertices = DSALinkedList()  # Linked list to store all vertices

    def add_vertex(self, label):
        """Adds a new location (node) if it doesn't already exist."""
        if not self.find_vertex(label):
            self.vertices.insert_last(GraphNode(label))

    def find_vertex(self, label):
        """Finds and returns a vertex by label if it exists."""
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex
        return None

    def add_edge(self, start_label, end_label, distance):
        """Adds a road (edge) with distance between two locations if it doesn't already exist with the same distance."""
        start_vertex = self.find_vertex(start_label)
        end_vertex = self.find_vertex(end_label)
        
        if start_vertex and end_vertex:
            # Check if an edge already exists with the same distance
            existing_distance = self.get_edge_distance(start_label, end_label)
            if existing_distance is not None and existing_distance == distance:
                print(f"Edge between {start_label} and {end_label} already exists with the same distance ({distance}).")
                return
            # If the edge doesn't exist or the distance is different, add/update it
            start_vertex.add_edge(end_vertex, distance)  # Add end as neighbor to start
            end_vertex.add_edge(start_vertex, distance)  # Add start as neighbor to end (undirected)
            print(f"Edge added between {start_label} and {end_label} with distance {distance}.")
        else:
            print("Error: One or both locations not found in the graph.")

    def get_edge_distance(self, start_label, end_label):
        """Returns the distance if an edge exists between start_label and end_label; otherwise, returns None."""
        start_vertex = self.find_vertex(start_label)
        if start_vertex:
            for neighbor, distance in start_vertex.adjacency_list:
                if neighbor.label == end_label:
                    return distance
        return None

    def get_neighbors(self, label):
        """Returns a list of neighboring locations for a given location."""
        vertex = self.find_vertex(label)
        if vertex:
            return [(neighbor[0].label, neighbor[1]) for neighbor in vertex.adjacency_list]
        else:
            print("Error: Location not found.")
            return []

    def display_graph(self):
        """Displays the graph structure as an adjacency list."""
        for vertex in self.vertices:
            neighbors = [(neighbor[0].label, neighbor[1]) for neighbor in vertex.adjacency_list]
            print(f"{vertex.label} -> {neighbors}")

    def clear_visited(self):
        """Clears the visited status of all vertices."""
        for vertex in self.vertices:
            vertex.visited = False

    def is_path(self, source_label, destination_label):
        """Checks if a path exists between two locations using BFS."""
        source = self.find_vertex(source_label)
        destination = self.find_vertex(destination_label)

        if not source or not destination:
            print("Error: One or both locations not found.")
            return False
        elif source == destination:
            return True

        self.clear_visited()

        queue = DSAQueue()
        queue.enqueue(source)
        source.visited = True

        while not queue.is_empty():
            current = queue.dequeue()
            if current == destination:
                return True

            for neighbor, _ in current.adjacency_list:
                if not neighbor.visited:
                    neighbor.visited = True
                    queue.enqueue(neighbor)

        return False
