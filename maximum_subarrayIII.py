#coding=UTF-8

"""
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Example
Given [-1,4,-2,3,-2,3], k=2, return 8

Note
The subarray should contain at least one number

""" 

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        