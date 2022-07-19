class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hashmap = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in hashmap:                              
                hashmap[key] = [s]
            else:
                hashmap[key].append(s)   
        
        ans = [hashmap[val] for val in hashmap]        
        
        return ans