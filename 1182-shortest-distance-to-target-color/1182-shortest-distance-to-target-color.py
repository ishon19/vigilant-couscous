class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # create a hashmap
        hashmap = collections.defaultdict(list)
        for i, c in enumerate(colors): 
            hashmap[c].append(i)
            
        ans = []
        
        for i, (target, color) in enumerate(queries):
            if color not in hashmap:
                ans.append(-1)
                continue
            
            idx_list = hashmap[color]
            insert_idx = bisect.bisect_left(idx_list, target)
            
            left = abs(idx_list[max(insert_idx - 1, 0)] - target)
            right = abs(idx_list[min(insert_idx, len(idx_list) - 1)] - target)
            ans.append(min(left, right))
        
        return ans