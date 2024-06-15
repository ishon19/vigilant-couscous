class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []

        for ele in arr2:
            cnt = arr1.count(ele)
            res += [ele] * cnt
        
        res2 = []
        for ele in arr1:
            if arr2.count(ele) == 0:
                res2 += [ele]
        
        return res + sorted(res2)
            