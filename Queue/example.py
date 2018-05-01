# Import Queue
from queue import Queue

# Create a new class to model investment accounts
class InvestmentAccount:

    def __init__(self, name_of_owner, portfolio):
        self.name_of_owner = name_of_owner
        self.portfolio = portfolio

# Create some instances
account1 = InvestmentAccount("Bill", {"AAPL" : 10, "INTC" : 20})
account2 = InvestmentAccount("Jill", {"KO" : 30, "MSFT" : 40})
account3 = InvestmentAccount("Phil", {"T" : 100, "F" : 200})
account4 = InvestmentAccount("Will", {"TGT" : 150, "WMT" : 45})

# Create a queue with a tuple containing our accounts
queue = Queue((account1, account2, account3))

# Iterate over queue
for i in queue:
    first, second = i.portfolio.items()
    print(i.name_of_owner + " owns " + str(first[1]) + " shares of " + first[0]
          + " and " + str(second[1]) + " shares of " + second[0])

# Add 10 shares of AAPL to each account in order of the queue
for i in queue:
    portfolio = i.portfolio
    if "AAPL" in portfolio:
        portfolio["AAPL"] += 10
    else:
        portfolio["AAPL"] = "10"

# Add an account to the queue
queue.push(account4)

# Print whats next in the queue
print(queue.peek().name_of_owner + "'s account is next in queue")

# pop() returns and removes the next item in the stack
print(queue.pop().name_of_owner + "'s account was popped from queue")

# Check if something is in the queue
print("Bill's account is still in the queue: " + str(queue.contains(account1)))

# Reverse the queue
queue.reverse()

# clear/empty the queue
queue.clear_queue()

# Make sure it's emepty
print("Queue is empty: " + str(queue.is_empty()))
