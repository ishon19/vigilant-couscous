class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __add_node(self, node):
        save = self.head.next
        save.prev = node
        node.next = save
        node.prev = self.head
        self.head.next = node
    
    def __remove_node(self, node):
         next = node.next
         prev = node.prev
         prev.next = next
         next.prev = prev
        
    def _move_to_head(self, node):
        self.__remove_node(node)
        self.__add_node(node)
    
    def _pop_tail(self):
        prev = self.tail.prev
        self.__remove_node(prev)
        return prev
        

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        else:
            # move this node to the head
            self._move_to_head(node)        
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
           # update the key value and move it to the head
           node.val = value
           self._move_to_head(node)
        else:
            # create a node
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.__add_node(newNode)

            if len(self.cache) > self.capacity:
                # remove node from the end
                # evict node
                tail = self._pop_tail()
                del self.cache[tail.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)