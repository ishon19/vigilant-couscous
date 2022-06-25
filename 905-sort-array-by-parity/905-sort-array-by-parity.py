class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        A = nums
        i,j = 0,1
        while j<len(A):
            if A[i]%2!=0 and A[j]%2!=0:
                j += 1
            elif A[i]%2!=0 and A[j]%2==0:
                A[i],A[j] = A[j],A[i]
                i+=1
                j+=1
            elif A[i]%2==0:
                i += 1
                j += 1
            else:
                j += 1
                    
        return A