# Import BinarySearchTree
from binary_search_tree import BinarySearchTree

# Create a new class to model rappers.
class Rapper:

    def __init__(self, name, best_songs):
        self.name = name
        self.best_songs = best_songs

    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name

# Create some instances
mineo = Rapper("Andy Mineo", ("Shallow", "Death Has Died", "Curious"))
jgivens = Rapper("JGivens", ("Super Lowkey", "March 10th and a Third", "Butterfly Stance"))
kb = Rapper("KB", ("Mr. Pretender", "Ima Just Do It", "Primetime"))
trip = Rapper("Trip Lee", ("Who He Is", "Bear With You", "Lazarus"))

# Create a BinarySearchTree
tree = BinarySearchTree((mineo, jgivens, kb))

# Iterate over the tree like this
for rapper in tree:
    first, second, third = rapper.best_songs
    print(rapper.name + "'s best songs are: " + first + ", " + second +
          ", and " + third + ".")
print()

# To add a rapper to our tree
tree.add(trip)

# To get elements in the tree
print("First rapper in tree: " + tree.get_first().name)
print("Last rapper in tree: " + tree.get_last().name)

# To remove an object
tree.remove(mineo)

# To check if an object is in the tree use contains()
print("Mineo was removed: " + str(tree.contains(mineo)))

# To get the size of the tree use size()
print("Tree has " + str(tree.size()) + " rappers in it.")

# To clear/empty the tree
tree.clear()

# To make sure the tree is empty
print("Tree is now empty: " + str(tree.is_empty()))
