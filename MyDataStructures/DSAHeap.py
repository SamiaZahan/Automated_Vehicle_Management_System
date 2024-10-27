import numpy as np
# DSAHeapEntry class definition
class DSAHeapEntry:
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


# DSAHeap class definition
class DSAHeap:
    def __init__(self, size):
        self.heap = np.empty(size, dtype=object)
        self.count = 0

    def add(self, priority, value):
        if self.count >= len(self.heap):
            raise IndexError("Heap is full")
        
        new_entry = DSAHeapEntry(priority, value)
        self.heap[self.count] = new_entry
        self.trickleUp(self.count)
        self.count += 1

    def remove(self):
        if self.count == 0:
            raise IndexError("Heap is empty")
        
        root = self.heap[0]
        self.count -= 1
        self.heap[0] = self.heap[self.count]
        self.heap[self.count] = None  # Clear the last element
        self.trickleDown(0)
        return root

    def trickleUp(self, index):
        parentIdx = (index - 1) // 2
        if index > 0 and self.heap[index].getPriority() > self.heap[parentIdx].getPriority():
            self.heap[index], self.heap[parentIdx] = self.heap[parentIdx], self.heap[index]
            self.trickleUp(parentIdx)

    def trickleDown(self, index):
        leftChildIdx = 2 * index + 1
        rightChildIdx = 2 * index + 2
        largest = index

        if leftChildIdx < self.count and self.heap[leftChildIdx].getPriority() > self.heap[largest].getPriority():
            largest = leftChildIdx
        if rightChildIdx < self.count and self.heap[rightChildIdx].getPriority() > self.heap[largest].getPriority():
            largest = rightChildIdx

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.trickleDown(largest)

    def heapify(self, entries):
        # Initialize the heap with the provided entries
        self.count = len(entries)
        self.heap = np.array(entries, dtype=object)
        for i in range(self.count // 2 - 1, -1, -1):
            self.trickleDown(i)

    def heapSort(self):
      sorted_list = np.empty(self.count, dtype=object)  
      original_count = self.count

      for i in range(original_count - 1, -1, -1):
          self.heap[0], self.heap[i] = self.heap[i], self.heap[0]  
          sorted_list[original_count - 1 - i] = self.heap[i]  # Add the sorted element to the numpy array
          self.count -= 1
          self.trickleDown(0)  # Restore the heap property
      sorted_list = sorted_list[::-1]
      return sorted_list
