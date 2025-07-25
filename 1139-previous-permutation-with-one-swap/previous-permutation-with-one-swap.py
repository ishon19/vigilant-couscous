class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        peak = None

        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                peak = i
                break
        
        if peak is None:
            return arr
        
        for i in range(len(arr)-1, peak, -1):
            if arr[i] < arr[peak] and arr[i] != arr[i-1]:
                arr[i], arr[peak] = arr[peak], arr[i]
                break
        
        return arr