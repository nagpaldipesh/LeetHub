class MyHashMap:

    def __init__(self):
        self.size = 1011  # Prime number to reduce collisions
        self.bucket = [[] for _ in range(self.size)] 

    def get_hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash = self.get_hash(key)
        
        for i, (k,v) in enumerate(self.bucket[hash]):
            if k == key:
                self.bucket[hash][i] = (key, value)
                return

        self.bucket[hash].append((key, value))

    def get(self, key: int) -> int:
        hash = self.get_hash(key)
        for (k, v) in self.bucket[hash]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash = self.get_hash(key)
        self.bucket[hash] = [(k, v) for (k, v) in self.bucket[hash] if k != key]
