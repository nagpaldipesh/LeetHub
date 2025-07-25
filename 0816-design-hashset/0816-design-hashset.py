class MyHashSet:
    
    def __init__(self):
        self.size = 1011 # Prime Number
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = self.get_index(key)
        
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.get_index(key)
        
        if key in self.buckets[index]:
            return True
        return False

    def get_index(self, key: int) -> int:
        return key % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)