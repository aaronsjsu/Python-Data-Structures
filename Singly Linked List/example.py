# Import linked_list.py
from linked_list import LinkedList

# Create a new class Person
class Person:

    def __init__(self, name, age, hobbys):
        self.name = name
        self.age = age
        self.hobbys = hobbys

    def __str__(self):
        """Specifies how to print Person objects."""
        to_print = ("Name: " + self.name + ", Age: " +
                    str(self.age) + ", Hobbys: " + str(self.hobbys))
        return to_print

# Create new people
bob = Person("Bob", 25, ("burping", "biking", "breaking"))
rob = Person("Rob", 35, ("riding", "reading", "reviewing"))
tob = Person("Tob", 45, ("training", "teaching", "talking"))

# Create LinkedList and fill it with a list containing each person
list_of_people = LinkedList([bob, rob, tob])

# Loop through LinkedList
for person in list_of_people:
    print(person.name + " is " + str(person.age) + " years old.")

# Add more people to our list
pob = Person("Pob", 65, ("playing", "praying", "paying"))
lob = Person("Lob", 15, ("laughing", "lauding", "laying"))
nob = Person("Nob", 55, ("naying", "naming", "nailing"))
list_of_people.add_to_end(pob)
list_of_people.add_to_beginning(lob)
list_of_people.insert_after(tob, nob)

# Print our list to the console
list_of_people.print_list()

# Reverse our list
list_of_people.reverse()
list_of_people.print_list()

# Manipulate our list
list_of_people.remove(lob) # Removes lob from list
print("List contains lob: " + str(list_of_people.contains(lob))) # Check if lob is gone
also_bob = list_of_people.poll_first() # poll() methods remove and return a list element
also_tob = list_of_people.poll(1) # Can poll() from an index too
also_pob = list_of_people.poll_last()
list_of_removed_people = [also_bob, also_pob, also_tob, lob]
for person in list_of_removed_people: # Make sure our people left the list.
    if (list_of_people.contains(person)):
        print("Our list contains something it shouldn't")
print("Checking list: ") # Take a look at the list now.
list_of_people.print_list()
for i in list_of_removed_people: # Now add our people back into the list by age.
    for j in list_of_people: # Notice that each age is separated by 10.
        if (i.age >= list_of_people.peek_first().age + 10):
            # The peek() methods return (without removing) a list item
            list_of_people.add_to_beginning(i)
            break
        elif (i.age == j.age - 10):
            list_of_people.insert_after(j, i)
            break
print("Checking list again: ") # Now lets look at the list!
list_of_people.print_list()

# Lastly, clear our list
list_of_people.clear_list()

# Note: there are other methods in linked_list.py that are not used here.
