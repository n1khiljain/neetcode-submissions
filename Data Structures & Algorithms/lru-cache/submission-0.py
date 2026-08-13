class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        # Left = LRU, Right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove from list
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    # insert at right to MRU
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

        
    def get(self, key: int) -> int:
        # cache is key -> node
        # everytime we perform get, that becomes MRU, remove then insert
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            val = self.cache[key].val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove LRU and delete from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)