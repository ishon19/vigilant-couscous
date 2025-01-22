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
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_node(self, node):
        save = self.head.next
        self.head.next = node
        node.next = save
        node.prev = self.head
        save.prev = node
        

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
    
    def pop_tail(self):
        prev = self.tail.prev
        self.remove_node(prev)
        return prev

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        # move to the head
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            # move this to the head
            node.value = value
            self.move_to_head(node)
            return
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.add_node(newNode)

            # do a size check 
            if len(self.cache) > self.capacity:
                # pop tail
                tail = self.pop_tail()
                del self.cache[tail.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
