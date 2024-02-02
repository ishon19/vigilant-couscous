class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # pattern = "123456789"
        # res = []

        # for i in range(len(str(low)), len(str(high)) + 1):
        #     for window in range(len(pattern) - i + 1):
        #         num = int(pattern[window: window + i])
        #         if num in range(low, high + 1):
        #             res.append(num)
        # return res
        
        # fastest code
        t = '123456789'
        l = []
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                if low <= int(t[i:j]) <= high:
                    l.append(int(t[i:j]))
        return sorted(l)
            

