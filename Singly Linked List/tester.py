# This file tests methods from linked_list.py
import linked_list

# Create new LinkedList
list = linked_list.LinkedList()

# Test that it iterates properly
other_list = linked_list.LinkedList()
for i in range(10):
    other_list.add_to_end(i)
for i in other_list:
    print(str(i) + " ", end="")
print()
iterable = iter(other_list)
for i in range(10):
    print(str(next(iterable)), end=" ")
print("\nExpected: 0 1 2 3 4 5 6 7 8 9")
print("-----")

# Test method add_to_beginning()
list.add_to_beginning(1)
list.print_list()
print("expected: 1")
print("-----")
list.add_to_beginning(0)
list.print_list()
print("expected: 0 1")
print("-----")

# Test method add_to_end()
list.add_to_end(3)
list.print_list()
print("expected: 0 1 3")
print("-----")

# Test method insert_after()
list.insert_after(1, 2)
list.print_list()
print("expected: 0 1 2 3")
print("-----")
try:
    list.insert_after(5, 6)
except Exception as e:
    print("Got exception: " + str(e))
print("Expected exception: Previous node does not exist")
print("-----")

# Test method contains()
print("Contains 4: " + str(list.contains(4)))
print("Expected: False")
print("Contains 3: " + str(list.contains(3)))
print("Expected: True")
print("-----")

# Test method size()
print("List size: " + str(list.size()))
print("Expected list size: 4")
print("-----")

# Test method remove()
list.remove(1)
list.print_list()
print("expected: 0 2 3")
print("-----")
try:
    list.remove(5)
except Exception as e:
    print("Got exception: " + str(e))
print("Expected exception: Item to remove does not exist")
print("-----")

# Test method clear_list()
list.clear_list()
list.print_list()
if list.size() is 0:
    print("List cleared")
print("-----")

# Test method reverse()
for i in range(10):
    list.add_to_end(i)
list.reverse()
list.print_list()
print("Expected: 9 8 7 6 5 4 3 2 1 0")
list.clear_list()
print("-----")

# Test peek methods
for i in range(10):
    list.add_to_end(i)
print(list.peek(1))
print("Expected: 1")
print(list.peek_first())
print("Expected: 0")
print(list.peek_last())
print("Expected: 9")
print("-----")

# Test poll methods
print(list.poll(5))
print("Expected: 5")
list.print_list()
print("Expected: 0 1 2 3 4 6 7 8 9")
print(str(list.poll_last()) + str(list.poll_first()))
print("Expected: 90")
list.print_list()
print("Expected: 1 2 3 4 6 7 8")
print("-----")

# Test remove methods
list.remove_last()
list.remove_first()
list.remove_last()
list.print_list()
print("Expected: 2 3 4 6")
print("-----")

# ----- Test adding lists and tuples -----
# Test insert_after()
list.clear_list()
for i in range(6):
    list.add_to_end(i)
list_to_add = [2, 2, 2]
tuple_to_add = (6, 6, 6)
list.insert_after(0, list_to_add)
list.insert_after(4, tuple_to_add)
list.print_list()
print("Expected: 0 2 2 2 1 2 3 4 6 6 6 5")
print("-----")

# Test adding LinkedList in LinkedList constructor
list.clear_list()
for i in range(5):
    list.add_to_end(i)
list2 = linked_list.LinkedList(list)
list2.add_to_end(5)
list2.print_list()
print("Expected: 0 1 2 3 4 5")
list.print_list()
print("Expected: 0 1 2 3 4")
print("-----")

# Test adding list/tuple in constructor
list_constructed_with_list = linked_list.LinkedList(list_to_add)
list_constructed_with_tuple = linked_list.LinkedList(tuple_to_add)
list_constructed_with_tuple.print_list()
print("Expected: 6 6 6")
list_constructed_with_list.print_list()
print("Expected: 2 2 2")
print("-----")

# Test add_to_end() and add_to_beginning()
list.add_to_beginning(tuple_to_add)
list.add_to_end(list_to_add)
list.print_list()
print("Expected: 6 6 6 0 1 2 3 4 2 2 2")
