from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum([x for x in salary if x!=min(salary) and x!=max(salary)])/(len(salary)-2)