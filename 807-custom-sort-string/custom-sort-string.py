class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charArr = list(s)
        charArr.sort(key=lambda x: order.index(x) if x in order else -1)
        # print(charArr)
        return ''.join(charArr)