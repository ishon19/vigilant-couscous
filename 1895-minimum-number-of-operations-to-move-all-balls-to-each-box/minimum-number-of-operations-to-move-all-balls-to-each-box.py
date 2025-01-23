class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        for i in range(len(boxes)):
            if boxes[i] == "1":
                for j in range(len(boxes)):
                    res[j] += abs(j - i)
        return res