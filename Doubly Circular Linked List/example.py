# Import linked_list.py and datetime
from linked_list import LinkedList
from datetime import datetime

# Create a new class Book
class Book:

    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        """Specifies how to print Book objects."""
        return self.title + ", " + self.author + ", " + str(self.year_published)

# Create new books
thg = Book("The Hunger Games", "Suzanne Collins", 2008)
tkam = Book("To Kill a Mockingbird", "Harper Lee", 1960)
podg = Book("The Picture of Dorian Gray", "Oscar Wilde", 1890)

# Create LinkedList and fill it with a list containing each book
list_of_books = LinkedList([thg, tkam, podg])

# Loop through LinkedList
for book in list_of_books:
    print(book.title + " is "
          + str(datetime.now().year - book.year_published) + " years old.")
print()

# Add more books to our list
tpp = Book("The Pilgrim's Progress", "John Bunyan", 1678)
tsl = Book("The Screwtape Letters", "C. S. Lewis", 1942)
list_of_books.add_to_end(tpp)
list_of_books.insert_after(tkam, tsl)

# Print our list to the console
list_of_books.print_list()

# Reverse our list
list_of_books.reverse()
list_of_books.print_list()

# Manipulate our list
list_of_books.remove(thg) # Removes thg from list
print("List still contains 'The Hunger Games': "
      + str(list_of_books.contains(thg))) # Check if thg is indeed gone

also_tpp = list_of_books.poll_first() # poll() methods remove and return a list element
also_tkam = list_of_books.poll(1) # Can poll() from an index too
also_podg = list_of_books.poll_last()
list_of_removed_books = [also_tpp, also_tkam, also_podg, thg]

for book in list_of_removed_books: # Make sure our books left the list.
    if (list_of_books.contains(book)):
        print("Our list contains something it shouldn't")
print("Checking list: ") # Take a look at the list now.
list_of_books.print_list()

for i in list_of_removed_books: # Now add our books back into the list sorted by year.
    for j in range(0, list_of_books.size()):
        if (i.year_published <= list_of_books.peek_first().year_published):
            list_of_books.add_to_beginning(i)
            continue
        if (i.year_published >= list_of_books.peek(j).year_published):
            if (list_of_books.size() > j + 1):
                if (i.year_published <= list_of_books.peek(j + 1).year_published):
                    list_of_books.insert_after(list_of_books.peek(j), i)
            else:
                list_of_books.add_to_end(i)

print("Checking list again: ") # Now lets look at the list again.
list_of_books.print_list()

# Lastly, clear our list
list_of_books.clear_list()

# Note: there are other methods in linked_list.py that are not used here.
