class LRUCache:

    def __init__(self, capacity: int):
        self.time = {} # (key: time)
        self.queue = deque() # LRU (key, time)
        self.values = {}
        self.capacity = capacity
        self.t = 0

    def get(self, key: int) -> int:
        if key in self.values:
            self.queue.append((key, self.t))
            self.time[key] = self.t
            self.t += 1
            return self.values[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                evictKey, evictTime = self.queue.popleft()
                while evictTime != self.time[evictKey]:
                    evictKey, evictTime = self.queue.popleft()
                del self.values[evictKey]
                del self.time[evictKey]
        self.queue.append((key, self.t))
        self.values[key] = value
        self.time[key] = self.t
        self.t += 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)