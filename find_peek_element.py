"""
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak

Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)

Note
The array may contains multiple peeks, find any of them.

Challenge
Time complexity O(logN)

"""


class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    """
    I am not coming up with this method
    actually it is a typical binary search problem, based on the assumption
    of the problem, we can make sure we will find one solution using 
    binary search, since we keep narrow down the possible areas of the 
    peak element, we don't care to find alll the peak values.

    """
    def findPeak(self, A):
        # write your code here









# java codee:
"""
 1 class Solution {
 2     /**
 3      * @param A: An integers array.
 4      * @return: return any of peek positions.
 5      */
 6     public int findPeak(int[] A) {
 7         if (A==null || A.length<3) return -1;
 8         int l = 1;
 9         int r = A.length - 2;
10         while (l <= r) {
11             int m = (l + r) / 2;
12             if (A[m]>A[m+1] && A[m]>A[m-1]) return m;
13             else if (A[m]<A[m+1] && A[m]>A[m-1]) {
14                 l = m + 1;
15             }
16             else {
17                 r = m - 1;
18             }
19         }
20         return -2;
21     }
22 }

"""

