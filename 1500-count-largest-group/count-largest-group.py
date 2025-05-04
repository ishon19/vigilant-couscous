class Solution:
    def getSum(self, num: int) -> int:
        total = 0
        while num:
            total += num % 10
            num = num // 10
        return total 

    def countLargestGroup(self, n: int) -> int:
        counts = defaultdict(list)

        for i in range(1, n+1):
            total = self.getSum(i)
            counts[total].append(i)

        max_size = len(max(counts.values(), key=len))
        result = 0

        for values in counts.values():
            if len(values) == max_size:
                result += 1
        
        return result