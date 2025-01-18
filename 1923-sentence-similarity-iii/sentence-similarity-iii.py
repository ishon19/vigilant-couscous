class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split(" ")
        l2 = sentence2.split(" ")

        dq1 = collections.deque(l1)
        dq2 = collections.deque(l2)

        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
                
        while dq1 and dq2 and dq1[-1] == dq2[-1]:
            dq1.pop()
            dq2.pop()
        
        return len(dq1) == 0 or len(dq2) == 0

        