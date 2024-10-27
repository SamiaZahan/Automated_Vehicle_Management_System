
from MyDataStructures.DSALinkedList import DSALinkedList

class DSAQueue:
    def __init__(self, capacity=None):
        self.queue = DSALinkedList()
        self.capacity = capacity

    def is_empty(self):
        return self.queue.is_empty()
      
    def is_full(self):
        if self.capacity is None:
            return False
        return self.queue.count >= self.capacity  # Checking size based on count in linked list

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue.insert_last(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.remove_first()

    def peek(self):
        return self.queue.peek_first()

    def size(self):
        return self.queue.count

    def show(self):
        self.queue.display()

        


