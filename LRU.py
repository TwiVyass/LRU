class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hashmap called cache to keep track of key, value pair

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        # left->next is poiting to right and right->prev is pointing to left

    # insert at right    
    def insert(self, node):
        prev, next = self.right.prev, self.right  # Fixed references to self.right
        prev.next = node  # Update previous node's next to the new node
        node.prev = prev  # Set new node's previous to the previous node
        node.next = next  # Set new node's next to the next node (self.right)
        next.prev = node  # Update next node's previous to the new node
 

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev     

    # -> int is that it returns int
    def get(self, key: int) -> int: 
        # we're looking for a key value, if found, return the value
        # Simultaneously have to switch to MRU (right) meaning inserting from right function
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1      

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # putting key, value node in hashmap to keep track
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
