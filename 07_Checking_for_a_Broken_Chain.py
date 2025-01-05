#imports the Block class from block.py
from block import Block

class Blockchain:
  def __init__(self):
    self.chain = []
    self.all_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    self.chain.append(new_block)

  def validate_chain(self):
    # цикл проверяющий всю цепочку на валидность
    for i in range(1, len(self.chain)):
      # рассматриваемый блок
      current = self.chain[i]
      # прошлый блок
      previous = self.chain[i-1]
      # проверка валидности, если хэш из блока не равен
      # сгенерированному при проверке хэшу - проверка не пройдена
      if current.hash != current.generate_hash():
        return False
      if current.previous_hash != previous.generate_hash():
        return False
    # если оба хэша совпадают - проверка пройдена
    return True
