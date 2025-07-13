class MyHashMap:

    def __init__(self):
        self.size = 1011
        self.bucket = [[] for _ in range(self.size)] 
        

    def put(self, key: int, value: int) -> None:
        hash = self.get_hash(key)
        
        self.remove(key)
            
        self.bucket[hash].append((key,value))
        

    def get(self, key: int) -> int:
        hash = self.get_hash(key)

        for (k, v) in self.bucket[hash]:
            if k == key:
                return v
            
        return -1

    def remove(self, key: int) -> None:
        hash = self.get_hash(key)

        for (k, v) in self.bucket[hash]:
            if k == key:
                self.bucket[hash].remove((k,v))

    def get_hash(self, key: int) -> int:
        return key % self.size
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)