#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        save = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = save
        save.prev = node
    
    def pop_tail(self):
        prev = self.tail.prev
        prev.prev.next = self.tail
        self.tail.prev = prev.prev
        return prev

    def add_node(self, node):
        save = self.head.next
        self.head.next = node
        save.prev = node
        node.next = save
        node.prev = self.head

    def get(self, key: int) -> int:
       node = self.cache.get(key, None)
       if node:
           self.move_to_head(node)
           return node.value
       return -1

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self.move_to_head(node)
        else:
            newNode = Node(key, value)
            self.add_node(newNode)
            self.cache[key] = newNode
            if len(self.cache) > self.size:
                node = self.pop_tail()
                del self.cache[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
