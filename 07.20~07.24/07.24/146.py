import time
import operator

class LRUCache:

    def __init__(self, capacity: int):
        self.chk = {}
        self.cache = {}
        self.size = capacity
        self.s_chk = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.chk[key] = time.time()
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.size:
            self.cache[key] = value
            self.chk[key] = time.time()
            print(self.chk)
        elif len(self.cache) == self.size and key in self.cache:
            self.cache[key] = value
            self.chk[key] = time.time()
            print(self.chk)
        elif len(self.cache) == self.size:
            self.s_chk = sorted(self.chk.items(), key=operator.itemgetter(1))
            del self.cache[self.s_chk[0][0]]
            print(self.s_chk)
            print(self.cache)
            del self.chk[self.s_chk[0][0]]
            self.cache[key] = value
            self.chk[key] = time.time()

# lc = LRUCache(2)
# lc.put(1,1)
# lc.put(2,2)
# lc.get(1)
# lc.put(3,3)
# lc.get(2)

lc = LRUCache(10)
lc.put(10,13)
lc.put(3,17)
lc.put(6,11)
lc.put(10,5)
lc.put(9,10)
lc.get(13)
lc.put(2,19)
lc.get(2)
lc.get(3)
lc.put(5,25)
lc.get(8)
lc.put(9,22)
lc.put(5,5)
lc.put(1,30)
lc.get(11)
lc.put(9,12)
lc.get(7)
lc.get(5)
lc.get(8)
lc.get(9)
lc.put(4,30)