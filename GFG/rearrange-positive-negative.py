'''
Problem Link
https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

Description
Given an array of positive and negative numbers, arrange them in an alternate fashion such that 
every positive number is followed by a negative and vice-versa maintaining the order of appearance. 
The number of positive and negative numbers need not be equal. If there are more positive numbers 
they appear at the end of the array. If there are more negative numbers, 
they too appear at the end of the array.
'''

'''
Naive solution
naive solution is to keep two separate data structures to keep track 

Optimal approach
The idea is to process the array from left to right. While processing, find the first out-of-place element 
in the remaining unprocessed array. An element is out of place if it is negative and at odd index (0-based index), 
or if it is positive and at even index (0-based index). Once we find an out-of-place element, we find the first element 
after it with an opposite sign. We right rotate the subarray between these two elements (including these two).
'''


def rearrange(arr):
    outOfPlace = -1
    for i in range(len(arr)):
        if outOfPlace>=0:
            # rotate only if the index and outOfPlace are of opposite signs
            if arr[i]>=0 and arr[outOfPlace]<0 or arr[i]<0 and arr[outOfPlace]>=0:
                arr = rightRotate(arr, outOfPlace, i)            