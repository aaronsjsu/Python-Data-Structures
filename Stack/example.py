# Import stack.py
from stack import Stack

# Create a new class Movie
class Movie:

    def __init__(self, title, reviews):
        self.title = title
        self.reviews = reviews

# Create some instances
star_trek1 = Movie("Star Trek: The Motion Picture", ("alright", "was a bummer"))
star_trek2 = Movie("Star Trek II: The Wrath of Kahn", ("amazing", "simply the best"))
star_trek3 = Movie("Star Trek III: The Search of Spock", ("forgettable", "could've been worse"))
star_trek4 = Movie("Star Trek IV: The Voyage Home", ("funny", "bad story, yet entertaining"))

# Create a stack with a list containing our movies
my_stack = Stack([star_trek1, star_trek2, star_trek3])

# Iterate over stack
for i in my_stack:
    print(i.title + " was " + i.reviews[0])
print()

# Add a movie to the stack
my_stack.push(star_trek4)

# Print whats on top of the stack
print(my_stack.peek().title + " was on the top of my stack")

# pop() gets the item at the top of the stack and removes it from stack
some_movie = my_stack.pop()
print("The movie " + some_movie.title + " was removed from the stack")

# Check if something is in the stack
print("Star Trek IV is in the stack: " + str(my_stack.contains(star_trek4)))

# Can reverse the order of the stack with
my_stack.reverse()

# Emtpy/clear the stack
my_stack.clear_stack()

# Make sure it's empty
print("The stack is empty: " + str(my_stack.is_empty()))
