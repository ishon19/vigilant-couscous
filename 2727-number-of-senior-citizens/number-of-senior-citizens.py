class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda a: a > 60, [int(d[-4:-2]) for d in details])))        