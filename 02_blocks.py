# In this exercise, we will be creating the default 
# constructor for the Block class in our Mini-Blockchain.

# import datetime library
from datetime import datetime

# print current date and time
print(datetime.now())


# creating our block with transactions, previous_hash, nonce(default=0), timestamp

class Block:
# default constructor for block class
  def __init__(self, transactions, previous_hash, nonce=0):
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.timestamp = datetime.now()
    pass
