class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # numset = set([1])
        # current_ugly = 1

        # for i in range(n):
        #     current_ugly = min(numset)
        #     numset.remove(current_ugly)

        #     numset.add(current_ugly * 2)
        #     numset.add(current_ugly * 3)
        #     numset.add(current_ugly * 5)
        
        # return current_ugly

        # simulate above using an array
        if n == 1: 1
        if n <= 0: return
        
        # pointers indicating the progress
        p2, p3, p5 = 0, 0, 0

        res = [0] * n
        res[0] = 1 # 1 is the lowest u-number
        for i in range(1, n):
            res[i] = min(res[p2]*2, res[p5]*5, res[p3]*3)
            if res[i] == res[p2]*2: p2+=1
            if res[i] == res[p3]*3: p3+=1
            if res[i] == res[p5]*5: p5+=1
        
        return res[-1]

            
