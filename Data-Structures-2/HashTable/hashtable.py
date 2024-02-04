class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        for i, (exist_key, exist_value) in enumerate(bucket):
            if exist_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        for exist_key, value in bucket:
            if exist_key == key:
                return value
        raise KeyError("Key not found")
    
    def remove(self, key):
        hash_value = self._hash(key)
        bucket = self.table[hash_value]

        for i, (exist_key, _) in enumerate(bucket):
            if exist_key == key:
                del bucket[i]
                return
            
        raise KeyError("Key not found")

    
htable = HashTable(6)
htable.insert("Sidharth", 45)
htable.insert("Arjun", 25)
htable.insert("Akash", 22)
htable.insert("Sudheesh", 20)
htable.insert("Shinas", 24)
htable.insert("Ansal", 18)


print(htable.get("Arjun"))

print(htable.table)