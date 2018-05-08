class Stack:
    """Creates a stack.

    This class creates a stack data structure, as defined
    in definition.txt.

    Attributes:
        stack: A list that stores the items in a Stack object.
    """

    def __init__(self, data=None):
        """Inits a stack.

        This initializes a stack. It can be initialized without
        an argument, in which case the stack is created empty, or
        it can be initialized with some initial data to add to it.

        Args:
            data: Optional data to add to the stack at creation.
                  It can be a single object or an iterable object.
        """
        self.stack = []
        if data is not None:
            self.push(data)

    def __iter__(self):
        """Allows the stack to be iterable."""
        # Reverse the list so that items are yielded as last in first out.
        reversed_list = list(reversed(self.stack))
        for i in reversed_list:
            yield i

    def push(self, data):
        """Add an item to the top/end of the stack.

        Args:
            data: The data to add to the stack, could be iterable.
        """
        try: # Try iterating if data is iterable
            for i in data:
                self.stack.append(i)
        except TypeError: # Else data isn't iterable
            if data is not None:
                self.stack.append(data)

    def peek(self):
        """Returns an item from the top of the stack."""
        if (len(self.stack) == 0):
            return
        data = self.stack.pop(len(self.stack) - 1)
        self.stack.append(data)
        return data

    def pop(self):
        """Returns and removes an item from the top of the stack."""
        if (len(self.stack) == 0):
            return
        return self.stack.pop(len(self.stack) - 1)

    def contains(self, data):
        """Checks if an item is in the stack.

        This checks if the stack contains a specified item. Returns
        true if it's in the stack, else returns false.

        Args:
            data: The data to look for in the stack.
        """
        if data is not None:
            for i in self.stack:
                if i is data:
                    return True
        return False

    def reverse(self):
        """Reverses the ordering of the stack."""
        self.stack = list(reversed(self.stack))

    def clear_stack(self):
        """Cleas/empties the stack."""
        self.stack = []

    def is_empty(self):
        """Checks if stack is empty, returns boolean."""
        return len(self.stack) == 0

    def print_stack(self):
        """Prints the stack in LIFO order."""
        for i in list(reversed(self.stack)):
            print(str(i), end=" ")
