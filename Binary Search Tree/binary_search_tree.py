class Node:
    """Node in a binary tree.

    This class represents a node in a binary tree. A node
    could be any form of data. Each node has two child nodes.

    Attributes:
        data: The data stored in each node.
        left: The node's left child node.
        right: The node's right child node.
    """

    def __init__(self, data):
        """Inits Node with its data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        """Enables node to be printed as a string of its data."""
        return str(self.data)


class BinarySearchTree:
    """Creates a binary search tree.

    This class creates a binary search tree as defined in definition.txt.
    It uses the Node class to store nodes and uses Node attributes
    (right and left) to manipulate the tree. Note that this tree isn't
    necessarily balanced.

    Attributes:
        root: The root node of the binary tree.
    """

    def __init__(self, data=None):
        """Inits the binary search tree.

        This initializes the binary tree object. Note that a binary
        tree can be initialized with an initial value for the root
        node, it can be initialized empty, or it can be initialized
        with an iterable object (including itself).

        Args:
            data: The data to initaialize the binary tree with,
                  default value is None.
        """
        self.root = None
        if data is not None:
            self.add(data)

    def __iter__(self):
        """Allows a binary search tree to be iterable."""
        binary_tree_list = self.tree_to_list(self.root, [])
        for i in binary_tree_list:
            yield i

    def tree_to_list(self, node, list):
        """This is a helper method for __iter__().

        This method recursively calls itself in order to convert
        the binary tree to a list in its natural order.

        Args:
            node: The node to start at, should be the root node when
                  first called.
        """
        if node:
            if node.left:
                self.tree_to_list(node.left, list)
            list.append(node.data)
            if node.right:
                self.tree_to_list(node.right, list)
        return list

    def add(self, data):
        """Adds a node to the tree.

        This adds data to the tree by first putting it into a node.
        It adds it based on the value of the data. If the node to add
        is greater than a node, then it will be placed to the right, if
        it's less than a node, then it's placed to the left.

        Args:
            data: The data to add to the binary tree. Could be iterable.
        """
        if data is None:
            return
        try: # Try iterating if data is iterable
            for i in data:
                # Need to deal with the case that the tree is empty.
                if self.root is None:
                    self.root = Node(i)
                else:
                    self.add_recurse(i, self.root)
        except TypeError: # Else data isn't iterable
            # Need to deal with the case that the tree is empty.
            if self.root is None:
                self.root = Node(data)
            else:
                self.add_recurse(data, self.root)

    def add_recurse(self, data, node):
        """Helper method for add() method.

        This adds a node to the tree. It is only called, and only meant
        to be called, within the add() method. It adds a node to the tree
        by comparing it to other nodes to find the proper place to insert
        the node. It does this by calling itself recursively.

        Args:
            data: The data to add to the binary tree.
            node: The node to compare the data to.
        """
        if (data < node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self.add_recurse(data, node.left)
        elif (data > node.data):
            if node.right is None:
                node.right = Node(data)
            else:
                self.add_recurse(data, node.right)
        else:
            # Else the data to add is the same as an existing node.
            # No duplicates allowed, so just return.
            return

    def remove(self, data):
        """Removes the specified data from the tree.

        Args:
            data: The data to remove.
        """
        self.remove_recurse(data, self.root, None)

    def remove_recurse(self, data, node, parent):
        """Helper method for remove().

        This removes a node from the tree. It does this by recursively
        calling itself to first find the node, and then removing the node
        by eliminating any references to that node.

        Args:
            data: The data to remove.
            node: The node to start searching at. Should be root node on
                  first method call.
            parent: The parent node of node.
        """
        if (data > node.data):
            self.remove_recurse(data, node.right, node)
        elif (data < node.data):
            self.remove_recurse(data, node.left, node)
        elif (data == node.data): # Found the node, now remove it.
            if node.right is None:
                if node.left is None:
                    # Means node to remove has no children.
                    if parent is not None: # Make sure node has a parent.
                        if node.data < parent.data:
                            # Node is the left child of it's parent.
                            parent.left = None
                        else: # Node is the right child of it's parent.
                            parent.right = None
                    else: # Else node has no parent.
                        # If node has no parent or children, then the node
                        # to remove is the root node.
                        self.root = None
                else: # Node to remove has a left child, no right child.
                    if parent is not None: # Make sure node has a parent.
                        # Connect the parent with node's child.
                        if node.data < parent.data:
                            # Node is the left child of it's parent.
                            parent.left = node.left
                        else: # Node is the right child of it's parent.
                            parent.right = node.left
                    else: # Else node has no parent.
                        self.root = node
            else: # Else node.right is not None.
                if node.left is None:
                    # Node to remove has a right child, no left child.
                    if parent is not None: # Make sure node has a parent.
                        # Connect the parent with node's child.
                        if node.data < parent.data:
                            # Node is the left child of it's parent.
                            parent.left = node.right
                        else: # Node is the right child of it's parent.
                            parent.right = node.right
                    else: # Else node has no parent.
                        self.root = node
                else: # Else two children.
                    # When the node to remove has two children, this is the
                    # mose complex case. The process to remove it follows:
                    # find minimum value in right subtree, replace value
                    # of node to remove with the minimum, then remove the minimum.
                    minimum = node.right
                    while mimimum.left is not None:
                        minimum = minimum.left
                    node.data = minimum.data
                    self.remove(minimum)
        else: # Else data supplied is not in the tree.
            return

    def get_first(self):
        """Returns the first (leftmost) item in the tree."""
        first_element = self.root
        while first_element.left is not None:
            first_element = first_element.left
        return first_element.data

    def get_last(self):
        """Returns the last (rightmost) item in the tree."""
        last_element = self.root
        while last_element.right is not None:
            last_element = last_element.right
        return last_element.data

    def contains(self, data):
        """Checks if an item is in the tree."""
        if self.root is None:
            return False
        else:
            return self.contains_recurse(data, self.root)

    def contains_recurse(self, data, node):
        """Helper method for contains().

        This method searches the tree for the specified data, and it
        return true if the data is in the tree, else false. It does
        this by recursively calling itself to search the tree efficiently.

        Args:
            data: The data to search for in the tree.
            node: The node to start searching at, should be root
                  node when first called.
        """
        if (data > node.data):
            if node.right is None:
                return False
            else:
                self.contains_recurse(data, node.right)
        elif (data < node.data):
            if node.left is None:
                return False
            else:
                self.contains_recurse(data, node.left)
        elif (data == node.data):
            return True
        else:
            return False

    def size(self):
        """Returns the number of nodes in the tree."""
        return len(self.tree_to_list(self.root, []))

    def clear(self):
        """Clears the tree (makes it empty)."""
        self.root = None

    def is_empty(self):
        """Checks if the tree is empty."""
        return self.root is None

    def print_tree(self):
        """Prints the tree to the console in order."""
        for element in self:
            if (len(str(element)) > 1):
                print(str(element))
            else: # Prints nodes on the same line if len(data) <= 1,
                  # this is for the sake of testing.
                print(str(element), end=" ")
        print()
