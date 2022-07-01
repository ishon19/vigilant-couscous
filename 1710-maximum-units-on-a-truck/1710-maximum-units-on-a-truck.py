class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        count = 0
        ans = 0
        for box in boxTypes:                                  
            for i in range(1, box[0]+1):
                if count<truckSize:
                    ans += box[1]
                    count += 1
        return ans
                