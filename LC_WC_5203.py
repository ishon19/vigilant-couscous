# Leetcode 5203 Count Artifacts that can be extracted
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        ans = 0
        visitedMap = {}
        for i in range(len(dig)):
            (r, c) = dig[i]
            for j in range(len(artifacts)):
               (r1, c1) = artifacts[j][:2]
               (r2, c2) = artifacts[j][2:]              
               if (r, c) == (r1, c1) and (r, c) == (r2, c2):
                    ans += 1
               elif (r, c) == (r1, c1) or (r, c) == (r2, c2):
                    if (r, c) == (r1, c1):
                        if visitedMap.get((r2, c2)) is None:
                            visitedMap[(r1, c1)] = True
                        else:
                            ans += 1
                    elif (r, c) == (r2, c2):
                            if visitedMap.get((r1, c1)) is None:
                                visitedMap[(r2, c2)] = True
                            else:
                                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.digArtifacts(n=5,
          artifacts=[[3, 1, 4, 1], [1, 1, 2, 2], [1, 0, 2, 0],
                     [4, 3, 4, 4], [0, 3, 1, 4], [2, 3, 3, 4]],
          dig=[[0, 0], [2, 1], [2, 0], [2, 3], [4, 3], [2, 4], [4, 1], [0, 2], [4, 0], [3, 1], [1, 2], [1, 3], [3, 2]]))
