class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Multiplicative Hash function"""
        constant_A = 0.6180339887
        key_numeric = hash(key)
        print(int(self.size * ((key_numeric * constant_A) % 1)) % self.size)
        return int(self.size * ((key_numeric * constant_A) % 1)) % self.size

    def insert(self, key, value):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for i, (ek, ev) in enumerate(bucket):
            if ek == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def remove(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        for i, (ek, ev) in enumerate(bucket):
            if ek == key:
                del bucket[i]
                return
        raise KeyError(f"Key {key} not found")
    
    def get(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for ek, ev in bucket:
            if ek == key:
                return ev
        raise KeyError(f"Key {key} not found")
    
    def load_factor(self):
        total_elements = sum(len(bucket)  for bucket in self.table)
        return total_elements / self.size

    
htable = HashTable(6)
htable.insert("Sidharth", "Machine Learning Engineer")
htable.insert("Arjun", "Data Scientist")
htable.insert("Sudheesh", "Business Magnete")
htable.insert("Akash", "Software Engineer")

print(htable.get("Akash"))

print(htable.table)

print(htable.load_factor())