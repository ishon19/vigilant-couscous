class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            sortedKey = "".join(sorted(list(s)))
            print(sortedKey)
            if sortedKey in hashmap:
                hashmap[sortedKey].append([sortedKey, s])
            else:
                hashmap[sortedKey] = [[sortedKey, s]]

        res = []

        for k, v in hashmap.items():
            vals = [o[1] for o in v]
            res.append(vals)
        
        return res
