class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False 
        
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False 

        index = self.val_to_index[val]
        last_index = len(self.nums)-1 

        if index != last_index:
            last_val = self.nums[last_index]
            self.nums[index] = last_val
            self.val_to_index[last_val] = index
        
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        random_idx = randint(0, len(self.nums)-1)
        return self.nums[random_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()