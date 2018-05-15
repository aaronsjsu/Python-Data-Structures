# Import Deque
from deque import Deque

# Create a new class to model movie characters
class MovieCharacter:

    def __init__(self, name, movie_name, traits):
        self.name = name
        self.movie_name = movie_name
        self.traits = traits

# Create some instances
spock = MovieCharacter("Spock", "Star Trek", ("Smart", "Logical", "Unemotional"))
marquis = MovieCharacter("Marquis Warren", "The Hateful Eight", ("Tough", "Daring", "Funny"))
john = MovieCharacter("John H. Miller", "Saving Private Ryan", ("Strong", "Brave", "Honorable"))
cobb = MovieCharacter("Dominick 'Dom' Cobb", "Inception", ("Smart", "Emotional", "Private"))

# Create a deque with a tuple containing our characters
deque = Deque((spock, marquis, john))

# Iterate over deque like this
for i in deque:
    first, second, third = i.traits
    print(i.name + " is in " + i.movie_name + ", and he is " + first
          + ", " + second + ", and " + third + ".")

# Add a character to the deque
deque.add_last(cobb)
deque.add_first(john)

# poll() methods return and remove a deque element
print(deque.poll_first().name + " was first in deque.")
print(deque.poll_last().name + " was last in deque.")

# peek() methods return (but don't remove) a deque element
print(deque.peek_first().name + " is now first in deque.")
print(deque.peek_last().name + " is now last in deque.")

# To check if something is in the deque
print("(T/F) Spock is in the list: " + str(deque.contains(spock)))

# To reverse the ordering of the deque
deque.reverse()

# Lastly, to clear/empty the deque
deque.clear()
