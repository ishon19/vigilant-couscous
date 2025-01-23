class Solution:
    def getNextNumber(self, num: int) -> int:
        num_sum = 0
        while num:
           temp = num % 10
           num //= 10
           num_sum += temp ** 2
        return num_sum 

    def isHappy(self, n: int) -> bool:
         fast = slow = n

         while True:
            slow = self.getNextNumber(slow)
            fast = self.getNextNumber(self.getNextNumber(fast))

            if fast == 1:
                return True
            elif fast == slow:
                return False