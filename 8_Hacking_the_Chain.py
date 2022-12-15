from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# создаем блокчейн
my_blockchain = Blockchain()

# добавляем транзакци в блок
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks()

# пытаемся подменить транзакцию
my_blockchain.chain[1].transactions = "fake_transactions"

# проверяем блокчейн на валидность
# из за подмененной транзакции результат отрицательный
my_blockchain.validate_chain()

