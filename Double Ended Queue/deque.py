class Node:
    """Node in a doubly linked list.

    This class represent a node in a doubly linked list, a
    node could store any type of data, and each node has
    a reference to the prev and next nodes.

    Attributes:
        data: Keeps track of the data in each node.
        prev: Points to the previous node in the linked list.
        next: Points to the next node in the linked list.
    """

    def __init__(self, data):
        """Inits Node with its data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        """Enables node to be printed as a string of its data."""
        return str(self.data)

class Deque:
    """Creates a deque.

    This class creates a deque data structure, as defined
    in definition.txt. It uses a doubly linked list to keep
    track of elements in the deque.

    Attributes:
        head: The head (beginning) node in the deque.
        tail: The tail (ending) node in the deque.
    """

    def __init__(self, data=None):
        """Inits a deque.

        This initializes a deque. It can be initialized without
        an argument, in which case the deque is created empty, or
        it can be initialized with some initial data to add to it.

        Args:
            data: Optional data to add to the queue at creation.
                  It can be a single object or an iterable object.
        """
        self.head = None
        self.tail = None
        if data is not None:
            self.add_last(data)

    def __iter__(self):
        """Allows the deque to be iterable."""
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

    def add_first(self, data):
        """Add an item to the beginning of the deque.

        Args:
            data: The data to add to the deque, could be iterable.
        """
        try: # Try iterating if data is iterable
            for i in data:
                self.add_first(i)
        except TypeError: # Else data isn't iterable
            if data is not None:
                new_node = Node(data)
                if self.head is None: # True if the deque is empty.
                    self.head = new_node
                    self.tail = new_node
                else: # Else deque not empty.
                    new_node.next = self.head
                    self.head.prev = new_node
                    if self.head.next is None:
                        # True if the deque only had one element.
                        self.tail = self.head
                    self.head = new_node

    def add_last(self, data):
        """Add an item to the end of the deque.

        Args:
            data: The data to add to the deque, could be iterable.
        """
        try: # Try iterating if data is iterable
            for i in data:
                self.add_last(i)
        except TypeError: # Else data isn't iterable
            if data is not None:
                new_node = Node(data)
                if self.head is None: # True if the deque is empty.
                    self.head = new_node
                    self.tail = new_node
                else: # Else deque not empty.
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    if self.tail.prev is None:
                        # True if the deque only had one element.
                        self.head = self.tail
                    self.tail = new_node

    def peek_first(self):
        """Returns the data in the head/first node."""
        if self.head is not None:
            return self.head.data

    def peek_last(self):
        """Returns the data in the tail/last node."""
        if self.tail is not None:
            return self.tail.data

    def poll_first(self):
        """Returns and removes the data in the head/first node."""
        if self.head is not None:
            first_node = self.head
            self.head = self.head.next
            if self.head is not None:
                # This is true if the deque isn't empty now.
                self.head.prev = None
            return first_node.data

    def poll_last(self):
        """Returns and removes the data in the tail/last node."""
        if self.tail is not None:
            last_node = self.tail
            self.tail = self.tail.prev
            if self.tail is not None:
                # This is true if the deque isn't empty now.
                self.tail.next = None
            return last_node.data

    def size(self):
        """Returns the size/length of the deque."""
        if self.head is None: # Deque is empty.
            return 0
        counter = 0
        current_node = self.head
        while current_node is not None:
            # This loops through entire deque.
            counter += 1
            current_node = current_node.next
        return counter

    def contains(self, data):
        """Checks if an item is in the deque.

        This checks if the deque contains a specified item. Returns
        true if it's in the deque, else returns false.

        Args:
            data: The data to look for in the deque.
        """
        if data is not None:
            for i in self:
                if i is data:
                    return True
        return False

    def reverse(self):
        """Reverses the ordering of the deque."""
        reversed_deque = Deque()
        for i in self:
            reversed_deque.add_first(i)
        self.head = reversed_deque.head
        self.tail = reversed_deque.tail

    def clear(self):
        """Clears/empties the deque."""
        self.head = None
        self.tail = None

    def is_empty(self):
        """Checks if deque is empty, returns a boolean."""
        return self.head == None

    def print_deque(self):
        """Prints deque elements in order."""
        for i in self:
            print(str(i), end=" ")
        print()
