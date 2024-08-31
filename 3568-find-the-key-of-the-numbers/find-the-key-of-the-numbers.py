class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def get_padded(num):
            s = str(num)
            if len(s) == 4:
                return s
            s = '0' * (4 - len(s)) + s
            return s
        
        def get_key(p1, p2, p3):
            k = ''
            for i in range(4):
                k += str(min(int(p1[i]), int(p2[i]), int(p3[i])))
            return int(k)

        p1, p2, p3 = get_padded(num1), get_padded(num2), get_padded(num3)
        k = get_key(p1, p2, p3)

        return k