# Basic Blockchain Implementation

This project involves the creation of a basic blockchain to understand the core principles behind blockchain technology. It was developed as part of a learning exercise while following a course.

## Features Implemented

1. **Transaction Management**:
   - Created and managed transactions as Python dictionaries.
   - Stored transactions in a mempool for further processing.

2. **Block Structure**:
   - Designed a `Block` class with attributes such as `transactions`, `previous_hash`, `nonce`, and `timestamp`.
   - Implemented functionality to generate a hash for a block using the SHA-256 algorithm.

3. **Blockchain Implementation**:
   - Built a `Blockchain` class to maintain a chain of blocks.
   - Added a genesis block (first block in the chain).
   - Implemented a method to add new blocks to the chain with proper linkage to the previous block's hash.

4. **Validation and Security**:
   - Implemented chain validation to ensure data integrity.
   - Used Proof-of-Work (PoW) to secure the blockchain by finding a valid hash that meets difficulty criteria.

5. **Proof-of-Work Mechanism**:
   - Added a difficulty level for PoW to simulate mining.
   - Implemented the process to find a valid hash by incrementing the nonce.

6. **Tamper Detection**:
   - Demonstrated how altering block data invalidates the blockchain.
   - Validated the chain after every update to check integrity.

## Code Highlights

### Transaction Example:
```python
transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'
}
mempool = [transaction1]
```

### Block Class:
```python
from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return sha256(block_contents.encode()).hexdigest()
```

### Blockchain Class:
```python
class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_block_hash)
        self.chain.append(new_block)

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generate_hash() or current.previous_hash != previous.hash:
                return False
        return True
```

## What I Learned

1. **Core Concepts of Blockchain**:
   - Understanding blocks, transactions, and hashes.
   - Importance of immutability and decentralization.

2. **Hashing with SHA-256**:
   - How to create a hash and its role in ensuring data integrity.

3. **Proof-of-Work**:
   - Concept of mining and nonce in blockchain.

4. **Data Security**:
   - How altering data affects the integrity of the entire blockchain.

5. **Object-Oriented Programming (OOP)**:
   - Applied OOP principles to structure the project.
   - Utilized constructors, methods, and attributes effectively.

## Future Improvements

- Implement a peer-to-peer network simulation.
- Add support for digital signatures to secure transactions.
- Explore other consensus algorithms like Proof-of-Stake (PoS).

---
This project was a hands-on learning experience that helped me grasp the fundamentals of blockchain technology. It serves as a foundational step for more advanced blockchain applications.
