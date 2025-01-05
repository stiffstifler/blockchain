from blockchain import Blockchain

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# создали блокчейн
local_blockchain = Blockchain()
# вывели блокчейн на екран
local_blockchain.print_blocks()

# добавляем блоки
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

local_blockchain.validate_chain()

# пробуем заменить значение в цепи

local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.print_blocks()
