transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = { 
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = { 
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = { 
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = { 
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = { 
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# add your code below

# create a transaction

my_transaction = {'amount': '777',
  'sender': 'Tiffany+',
  'receiver': 'Xavier+'}

# Add my_transaction to the mempool list

mempool.append(my_transaction)

# Create list and add three transactions. 
# This will allow us to prepare the transactions to be added to our future Block structure.

block_transactions = [transaction1, transaction2, transaction3]












