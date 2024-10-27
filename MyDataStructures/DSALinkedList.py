class DSAListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DSALinkedList:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.count = 0
        self.max_size = max_size

    def __iter__(self):
        self._current = self.head  
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration  
        else:
            value = self._current.value  
            self._current = self._current.next  
            return value  

    def insert_first(self, value):
        new_node = DSAListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def insert_last(self, value):
        new_node = DSAListNode(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def remove(self, value):
        """Remove the first occurrence of the node with the specified value."""
        current = self.head
        previous = None
        
        while current is not None:
            if current.value == value:
                # Case 1: Node to be removed is the head
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None  # The list is now empty
                # Case 2: Node to be removed is the tail
                elif current == self.tail:
                    self.tail = previous
                    if self.tail is not None:
                        self.tail.next = None
                    else:
                        self.head = None  # The list is now empty
                # Case 3: Node to be removed is in the middle
                else:
                    previous.next = current.next
                    if current.next is not None:
                        current.next.prev = previous

                self.count -= 1
                return True  # Node successfully removed
            previous = current
            current = current.next

        raise ValueError(f"Value '{value}' not found in the list")
    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.count -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.count -= 1
        return value

    def peek_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.head.value

    def peek_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.tail.value

    def is_empty(self):
        return self.head is None
