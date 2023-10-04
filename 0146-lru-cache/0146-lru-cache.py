class LRUCache:

    def __init__(self, capacity: int):
        self.stack = []
        self.ptr = 0
        self.capacity = capacity
        self.dct = {}

        

    def get(self, key: int) -> int:
        ans = -1
        if key in self.dct:
            ans = self.dct[key]
            self.stack.remove(key)
            self.stack.insert(0,key)
        return ans
        

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct[key] = value
            self.stack.remove(key)
            self.stack.insert(0,key)
        else:
            self.dct[key] = value
            if self.ptr == self.capacity:
                rem = self.stack.pop()
                self.dct.pop(rem)
                self.ptr -= 1
            self.stack.insert(0,key)
            self.ptr += 1
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)