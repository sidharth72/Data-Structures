class Hashtable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

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
        raise IndexError("cannot find the key")
    
    def get(self, key):
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for ek, ev in bucket:
            if ek == key:
                return ev
            
        raise IndexError('Cannot find the key')
    

htable = Hashtable(6)
htable.insert("Sidharth", "Machine Learning Engineer")
htable.insert("Shinas", "Devops Engineer")

print(htable.get("Sidharth"))