class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
         res = []
         stack = []

         for i in range(1, n+1):
             if target == stack:
                 break
             if i in target:
                 while stack and stack[-1] not in target:
                     stack.pop()
                     res.append("Pop")
                 stack.append(i)
                 res.append("Push")
             else:
                 stack.append(i)
                 res.append("Push")
         return res