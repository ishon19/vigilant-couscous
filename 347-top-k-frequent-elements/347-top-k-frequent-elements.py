class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(list)
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = [num]
            else:
                hashmap[num].append(num)
        print(hashmap)
        
        keys = [key for key in sorted(hashmap, key=lambda k: len(hashmap[k]), reverse=True)]
        
        return keys[:k]