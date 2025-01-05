#imports the Block class from block.py
from block import Block

class Blockchain:
    def __init__(self):
      # all the blocks inside the blockchain
      self.chain = []
      # all_transactions in block
      self.all_transactions = []
      # automatically create a Genesis Block
      self.genesis_block()
    
    def genesis_block(self):
      transactions = []
      previous_hash = "0"
      self.chain.append(Block(transactions, previous_hash))
      
