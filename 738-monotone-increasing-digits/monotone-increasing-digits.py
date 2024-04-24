class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # TLE
        # def isIncreasing(num):
        #     num_str = str(num)
        #     for i in range(1, len(num_str)):
        #         if int(num_str[i]) < int(num_str[i-1]):
        #             return False
        #     return True
        # for i in range(n, -1, -1):
        #     if isIncreasing(i):
        #         return i
        # return -1
        
        str_num = list(str(n))
        decIdx = len(str_num)
        for i in range(len(str_num)-1, 0, -1):
            if str_num[i] < str_num[i-1]:
                decIdx = i
                str_num[i-1] = str(int(str_num[i-1])-1)
        
        for i in range(decIdx, len(str_num)):
            str_num[i] = '9'
        
        return int(''.join(str_num))

