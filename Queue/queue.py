class Queue:
    """Creates a queue.

    This class creates a queue data structure, as defined
    in definition.txt.

    Attributes:
        queue: A list that stores the items in a queue object.
    """

    def __init__(self, data=None):
        """Inits a queue.

        This initializes a queue. It can be initialized without
        an argument, in which case the queue is created empty, or
        it can be initialized with some initial data to add to it.

        Args:
            data: Optional data to add to the queue at creation.
                  It can be a single object or an iterable object.
        """
        self.queue = []
        if data is not None:
            self.push(data)

    def __iter__(self):
        """Allows the queue to be iterable."""
        for i in self.queue:
            yield i

    def push(self, data):
        """Add an item to the end of the queue.

        Args:
            data: The data to add to the queue, could be iterable.
        """
        try: # Try iterating if data is iterable
            for i in data:
                self.queue.append(i)
        except TypeError: # Else data isn't iterable
            if data is not None:
                self.queue.append(data)

    def peek(self):
        """Returns an item from the beginning of the queue."""
        if (len(self.queue) == 0):
            return
        data = self.queue.pop(0)
        self.queue.insert(0, data)
        return data

    def pop(self):
        """Returns and removes an item from the beginning of the queue."""
        if (len(self.queue) == 0):
            return
        return self.queue.pop(0)

    def contains(self, data):
        """Checks if an item is in the queue.

        This checks if the queue contains a specified item. Returns
        true if it's in the queue, else returns false.

        Args:
            data: The data to look for in the queue.
        """
        if data is not None:
            for i in self.queue:
                if i is data:
                    return True
        return False

    def reverse(self):
        """Reverses the ordering of the queue."""
        self.queue = list(reversed(self.queue))

    def clear_queue(self):
        """Clears/empties the queue."""
        self.queue = []

    def is_empty(self):
        """Checks if queue is empty, returns a boolean."""
        return len(self.queue) == 0

    def print_queue(self):
        """Prints the queue in FIFO order."""
        for i in self.queue:
            print(str(i), end=" ")
