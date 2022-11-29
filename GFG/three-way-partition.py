'''
Problem Link
https://www.geeksforgeeks.org/three-way-partitioning-of-an-array-around-a-given-range/

Description

Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts. 
All elements smaller than lowVal come first. 
All elements in range lowVal to highVal come next. 
All elements greater than highVal appear in the end. 
'''

'''
Optimal approach
Go like dutch flag problem
'''


def threeWayPartition(arr, low, high):
    start = 0
    i = 0
    end = len(arr)-1

    # only till the right pointer matches
    while i < end:
        if arr[i] < low:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > high:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1


arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
threeWayPartition(arr, 10, 20)
print(arr)
