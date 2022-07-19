class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        hashmap = defaultdict(list)
        
        for s in strs:
            if "".join(sorted(s)) not in hashmap:                              
                hashmap["".join(sorted(s))] = [s]
            else:
                hashmap["".join(sorted(s))].append(s)   
        
        ans = [hashmap[val] for val in hashmap]        
        
        return ans