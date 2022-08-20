class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.least_recently_used = {}
        

    def get(self, key):
        if self.cache.get(key):
            self.least_recently_used[key] = 1 + self.least_recently_used.get(key, 0)
        return self.cache.get(key) if self.cache.get(key) else -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            if self.cache.get(key):
                self.cache[key] = value
            else:
                # remove lease used key value
                min_key = min(self.least_recently_used, key=self.least_recently_used.get)
                del self.least_recently_used[min_key]
                del self.cache[min_key]
                self.cache[key] = value

        self.least_recently_used[key] = 1 + self.least_recently_used.get(key, 0)

        
capacity = 2
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
# param_1 = obj.get(key1)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
