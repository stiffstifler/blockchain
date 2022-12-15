# import sha256
from hashlib import sha256

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# количество нулей которое должно быть у найденного нами хеша
difficulty = 2

# значение по умолчанию
nonce = 0

# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

# finding a proof that has 2 leading zeros
# пока в хэше пруф не будет 2х нулей выполняем цикл
while proof[:2] != '0'*difficulty:
  nonce += 1
  proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()

final_proof = proof
# printing final proof that was found
print(final_proof)

