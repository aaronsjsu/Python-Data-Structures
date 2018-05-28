# This file tests methods from linked_list.py
from linked_list import LinkedList

# Create new LinkedLists
list1 = LinkedList()
list2 = LinkedList((1, 2, 3))
list3 = LinkedList(list2)

# Test add methods
list3.insert_after(2, 2)
list3.insert_after(3, (4, 5))
list3.print_list()
print("Expected: 1 2 2 3 4 5")
print("-----")
list3.add_to_beginning(0)
list3.add_to_beginning((0, 0))
list3.print_list()
print("Expected: 0 0 0 1 2 2 3 4 5")
print("-----")
list3.add_to_end(6)
list3.add_to_end((7, 8))
list3.print_list()
print("Expected: 0 0 0 1 2 2 3 4 5 6 7 8")
print("-----")

# Test contains(), size(), remove(), clear_list()
print(list3.size())
print("Expected: 12")
print("-----")
list3.clear_list()
list3.print_list()
print((list3.size() == 0))
print("Expected: True")
print("-----")
print(list3.contains(1))
print("Expected: False")
print("-----")
list3.add_to_beginning(1)
print(list3.contains(1))
print("Expected: True")
print("-----")
list3.remove(1)
print(list3.size())
print("Expected: 0")
print("-----")

# Test peek methods
print(list2.peek(0) + list2.peek(1) + list2.peek(2))
print("Expected: 6")
print("-----")
list2.add_to_end(4)
print(list2.peek_last())
print("Expected: 4")
print("-----")
list2.add_to_beginning(0)
print(list2.peek_first())
print("Expected: 0")
print("-----")

# Test poll methods
print(list2.poll(0) + list2.poll(1) + list2.poll(2))
print("Expected: 6")
print("-----")
list2.add_to_end(4)
print(list2.poll_last())
print("Expected: 4")
print("-----")
print(list2.poll_last())
print("Expected: 3")
print("-----")
list2.add_to_beginning(0)
print(list2.poll_first())
print("Expected: 0")
print("-----")
list2.print_list()
print("Expected: 1")
print("-----")

# Test remove methods
list1.add_to_beginning((1, 2, 3, 4, 5))
list1.remove_last()
list1.remove_first()
list1.print_list()
print("Expected: 2, 3, 4")
print("-----")

# Test reverse(), print_reversed_list, copy_list,
list1.reverse()
list1.print_list()
print("Expected: 4, 3, 2")
print("-----")
list1.print_reversed_list()
print("Expected: 2, 3, 4")
print("-----")
list1_copy = list1.copy_list()
list1_copy.add_to_beginning(1)
print(list1_copy.peek_first() + list1.peek_first())
print("Expected: 5")
print("-----")