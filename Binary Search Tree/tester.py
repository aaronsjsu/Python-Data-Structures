from binary_search_tree import BinarySearchTree

tree = BinarySearchTree((1, 2, 4, 5))

# Test add()
tree.add(0)
tree.add(3)
tree.add(6)
tree.print_tree()
print("Expected: 0 1 2 3 4 5 6")
print("-----")

# Test remove()
tree.remove(0)
tree.remove(6)
tree.remove(3)
tree.print_tree()
print("Expected: 1 2 4 5")
print("-----")

# Test get_first()
print(tree.get_first())
print("Expected: 1")
print("-----")

# Test get_last()
print(tree.get_last())
print("Expected: 5")
print("-----")

# Test contains()
print(str(tree.contains(1)) + ", " + str(tree.contains(-1)))
print("Expected: True, False")
print("-----")

# Test size()
print(tree.size())
print("Expected: 4")
print("-----")

# Test clear() and is_empty()
tree.clear()
print(tree.is_empty())
print("Expected: True")
print("-----")
