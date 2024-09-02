class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        loss = sum(chalk)
        if k % loss == 0:
            return 0

        itr = k // loss
        start = k - itr * loss

        for i in range(len(chalk)):
            print(chalk[i], start)
            if chalk[i] > start:
                return i
            start -= chalk[i]
        return -1