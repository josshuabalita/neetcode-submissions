class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU_Cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.LRU_Cache:
            return -1
        self.LRU_Cache.move_to_end(key) # moves key to end meaning it is recently used
        return self.LRU_Cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.LRU_Cache:
            self.LRU_Cache.move_to_end(key)
        self.LRU_Cache[key] = value
        
        if len(self.LRU_Cache) > self.capacity:
            self.LRU_Cache.popitem(last=False) # drop the LRU

# T O(1)
# S O(n)