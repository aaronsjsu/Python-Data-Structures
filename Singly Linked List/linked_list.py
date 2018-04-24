class Node:
    """Node in a linked list.

    This class represent a node in a linked list, a node
    could be any form of data, and each node has a pointer.

    Attributes:
        data: Keep track of the data in each node.
        next: Points to the next node in the linked list.
    """

    def __init__(self, data):
        """Inits Node with its data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

    def __str__(self):
        """Enables node to be printed as a string of its data."""
        return str(self.data)


class LinkedList:
    """Creates a linked list.

    This class creates a linked list using the Node class
    to store nodes and uses Node attributes (data and next)
    to manipulate the linked list.

    Attributes:
        head: The head (beginning) node in the linked list.
    """

    def __init__(self, data=None):
        """Inits the linked list.

        This initializes the linked list object. Note that a
        linked list can be iniialized with an initial value in the
        head node, it can be initialized empty, or it can be
        initialized with a list, tuple, or another LinkedList object.

        Args:
            data: The data to initialize the linked list with, default
                  value is None.
        """
        if (type(data) is list or type(data) is tuple):
            # Deals with the case that data is a list or tuple.
            new_list = LinkedList()
            for i in data:
                new_list.add_to_end(i)
            self.head = new_list.head
        elif (type(data) is LinkedList):
            # Deals with the case that data is another LinkedList object.
            new_list = LinkedList()
            for i in data:
                new_list.add_to_end(i)
            self.head = new_list.head
        elif data is None:
            self.head = data
        else:
            self.head = Node(data)

    def __iter__(self):
        """Allows the linked list to be iterable."""
        element = self.head
        while (element): # Loops through each element in linked list.
            yield element.data
            element = element.next

    def insert_after(self, prev_node, new_data):
        """Adds data after a specified node.

        This method adds a new node(s) to the linked list after the
        location of the specified node. It takes some data
        as an argument (can be a list or tuple) and fills the node(s)
        with the data.

        Args:
            prev_node: The specified node to add a new node after.
            new_data: The new data to be added to the linked list.

        Raises:
            Exception: The prev_node variable is invalid.
        """
        if prev_node is None: # Makes sure prev_node is not None.
            raise Exception("Previous node is None")
            return
        prev_element = self.head
        while (prev_element.data != prev_node):
            # Loops until the previous element is found in the list.
            if prev_element.next is None:
                # Deals with the case that the previous node doesn't esist.
                raise Exception("Previous node does not exist")
                return
            prev_element = prev_element.next
        if (type(new_data) is list or type(new_data) is tuple):
            # Deals with the case that a list or tuple is to be added.
            # Create a new LinkedList and then insert it into existing one.
            inner_list = LinkedList(new_data)
            element = inner_list.head
            while (element.next):
                element = element.next
            element.next = prev_element.next
            prev_element.next = inner_list.head
        else:
            new_node = Node(new_data)
            new_node.next = prev_element.next
            prev_element.next = new_node

    def add_to_beginning(self, new_data):
        """Adds new node(s) at beginning.

        This method adds a new node(s) to the beginning of the
        linked list. It takes some data as an argument (can be a
        list or tuple) and fills the node(s) with the data.

        Args:
            new_data: The new data to be added to the linked list.
        """
        if (type(new_data) is list or type(new_data) is tuple):
            # Deals with the case that a list or tuple is to be added.
            # Create a new LinkedList and then add it at beginning of
            # existing one.
            inner_list = LinkedList(new_data)
            last_element = inner_list.head
            while (last_element.next):
                last_element = last_element.next
            last_element.next = self.head
            self.head = inner_list.head
        else:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node

    def add_to_end(self, new_data):
        """Adds new node(s) at end.

        This method adds a new node(s) to the end of the linked list.
        It takes some data as an argument (can be a list or tuple)
        and fills the node(s) with the data.

        Args:
            new_data: The new data to be added to the linked list.
        """
        if self.head is None:
            # Deals with the case that the linked list is empty.
            if (type(new_data) is list or type(new_data) is tuple):
                self.head = LinkedList(new_data).head
            else:
                self.head = Node(new_data)
        else:
            last_element = self.head
            while (last_element.next): # Loops until last element found.
                last_element = last_element.next
            # Call insert_after() to add new_data at end of linked list.
            self.insert_after(last_element.data, new_data)

    def contains(self, data):
        """Checks if item is in the linked list.

        This method searches the linked list to see if the specified
        item is in the list. It returns True if it is, else False.

        Args:
            data: The data to check if it's in the linked listself.
        """
        element = self.head
        while (element): # Loops through each element in the list.
            if element.data is data: # True if a match is found.
                return True
            element = element.next
        return False # Else no match found, return False.

    def size(self):
        """Returns the size/length of the linked list."""
        if self.head is None: # Checks if linked list is empty
            return 0
        count = 0
        element = self.head
        while(element): # Loops through each element
            count += 1 # Iterate count of elements
            element = element.next
        return count

    def remove(self, data_to_remove):
        """Removes the specified node.

        This method removes the specified node from the linked list.

        Args:
            data_to_remove: The data stored in a node that is to be removed.

        Raises:
            Exception: The data_to_remove variable is invalid.
        """
        if data_to_remove is None: # Makes sure data_to_remove is not None.
            raise Exception("Item to remove is None")
            return
        if (data_to_remove == self.head.data):
            # Deals with the case that the node to remove is the head.
            self.head = self.head.next
            return
        element = self.head
        while (element.next.data != data_to_remove):
            # Loops until the element before the element to remove is found.
            if (element.next.next == None):
                # Deals with the case that the node to remove doesn't exist.
                raise Exception("Item to remove does not exist")
                return
            element = element.next
        # Get rid of pointer/reference to the node to remove.
        element.next = element.next.next

    def peek(self, index):
        """Returns the data at a specified index.

        This method returns the data stored in a node at the specified
        index in the linked list. It does this without deleting the node.

        Args:
            index: The index of the desired node.

        Raises:
            Exception: The specified index does not exist.
        """
        if (index >= self.size() or index < 0): # Check that index is valid.
            raise Exception("Index out of bounds")
            return
        element = self.head
        counter = 0
        while (element): # Loops through each element
            if (counter == index): # True when index is reached
                return element.data
            counter += 1
            element = element.next

    def peek_first(self):
        """Returns the data in the head node."""
        return self.peek(0)

    def peek_last(self):
        """Returns the data in the tail/last node."""
        return self.peek(self.size() - 1)

    def poll(self, index):
        """Returns and removes the data at a specified indexself.

        This method returns the data stored in a node at the specified
        index in the linked list. It then removes the node from the
        linked list.

        Args:
            index: The index of the desired node.

        Raises:
            Exception: The specified index does not exist.
        """
        if (index >= self.size() or index < 0): # Check that index is valid.
            raise Exception("Index out of bounds")
            return
        element = self.head
        counter = 0
        while (element): # Loops through each element
            if (counter == index): # True when index is reached
                break
            counter += 1
            element = element.next
        temp = element # Store in a temporary variable before removing.
        self.remove(element.data)
        return temp.data

    def poll_first(self):
        """Returns and removes the head/first node data in the linked list."""
        return self.poll(0)

    def poll_last(self):
        """Returns and removes the tail/last node data in the linked list."""
        return self.poll(self.size() - 1)

    def remove_first(self):
        """Removes the head/first node in the linked list."""
        self.remove(self.peek_first())

    def remove_last(self):
        """Removes the tail/last node in the linked list."""
        self.remove(self.peek_last())

    def reverse(self):
        """Reverses the order of the linked list."""
        reversed_list = LinkedList()
        element = self.head
        while (element): # Loops through each element in linked list.
            # Add each element in reversed order to reversed_list.
            reversed_list.add_to_beginning(element.data)
            element = element.next
        self.head = reversed_list.head

    def clear_list(self):
        """Clears the linked list (makes it empty)."""
        self.head = None

    def copy_list(self, list_to_copy):
        """Returns a copy of the LinkedList object.

        Args:
            list_to_copy: The LinkedList object to copy.

        Raises:
            Exception: Argument is not an instance of LinkedList.
        """
        if (type(list_to_copy) is LinkedList):
            return LinkedList(list_to_copy)
        else:
            raise Exception("List to copy is not of type LinkedList.")

    def print_list(self):
        """Prints the linked list.

        This method prints the linked list elements in order.
        """
        element = self.head
        while (element): # Loops through the linked list.
            if (len(str(element.data)) > 1):
                print(str(element.data))
            else: # Prints nodes on the same line if len(data) <= 1,
                  # this is for the sake of testing.
                print(str(element.data), end=" ")
            element = element.next
        print() # Adds a new line at the end
