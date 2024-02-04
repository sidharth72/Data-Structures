class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)] # Chaining included

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        for i, (ek, ev) in enumerate(bucket):
            # Updating the indexes
            if ek == key:
                bucket[i] = (key, value)
                return
            # New insertion code
        bucket.append((key, value))

    def get(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        print(bucket)
        for ek, ev in bucket:
            if ek == key:
                return ev
        
        raise KeyError("Key not found")
    
    def remove(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for i, (ek, ev) in enumerate(bucket):
            if ek == key:
                del bucket[i]
                return
        raise KeyError("Key Not found")
    

htable = HashTable(6)
htable.insert("Sidharth", 21)
htable.insert("Arjun", 23)
htable.insert("Sudheesh", 12)

print(htable.get("Sudheesh"))

print(htable.table)






