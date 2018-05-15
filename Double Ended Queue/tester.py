from deque import Deque

deque1 = Deque()
deque2 = Deque([1, 2, 3, 4])
deque3 = Deque(1)

# Test add_first()
print("-----")
deque1.add_first(0)
deque2.add_first(0)
deque3.add_first(0)
deque1.print_deque()
deque2.print_deque()
deque3.print_deque()
print("Expected:")
print("0")
print("0 1 2 3 4")
print("0 1")


# Test add_last()
print("-----")
deque1.clear()
deque1.add_last(0)
deque2.add_last(5)
deque1.print_deque()
deque2.print_deque()
print("Expected:")
print("0")
print("0 1 2 3 4 5")

# Test peek_first()
print("-----")
print(deque1.peek_first() + deque2.peek_first())
print("Expected: 0")

# Test peek_last()
print("-----")
print(deque1.peek_last() + deque2.peek_last())
print("Expected: 5")

# Test poll_first()
print("-----")
print(deque3.poll_first() + deque3.poll_first())
print("Expected: 1")

# Test poll_last()
print("-----")
print(deque2.poll_last() + deque2.poll_last())
print("Expected: 9")

# Test size()
print("-----")
print(deque2.size())
print("Expected: 4")

# Test contains()
print("-----")
print(deque2.contains(0))
print("Expected: True")
print(deque2.contains(10))
print("Expected: False")

# Test reverse()
print("-----")
deque2.reverse()
deque2.print_deque()
print("Expected: 3 2 1 0")

# Test clear() and is_empty()
print("-----")
print(deque2.is_empty())
print("Expected: False")
deque2.clear()
print(deque2.is_empty())
print("Expected: True")