class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        res = []
        hand.sort()

        for i, num in enumerate(hand):
            if not len(res):
                res.append([num])
            else:
                appended = False
                for sub in res:
                    if len(sub) >= groupSize:
                        continue
                    if num not in sub:
                        # print('diff', abs(sub[-1] - num))
                        if abs(sub[-1] - num) > 1:
                            return False
                        sub.append(num)
                        appended = True
                        break
                if not appended:
                    res.append([num])          
        # print('res', res)
        for sub in res:
            if not len(sub) == groupSize:
                return False
        return True