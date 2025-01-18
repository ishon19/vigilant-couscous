class Solution:
    def handle_positive(self, arr, k):
        search_arr = arr + arr
        res = []
        for i in range(len(arr)):
            res.append(sum(search_arr[i+1:i+k+1]))
        return res
    
    def handle_negative(self, arr, k):
        search_arr = arr + arr
        res = []
        for i in range(len(search_arr)//2, len(search_arr)):
            res.append(sum(search_arr[i+k:i]))
        return res

    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            return self.handle_positive(code, k)
        return self. handle_negative(code, k)