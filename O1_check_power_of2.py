"""
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;
For n=5, return false;

Challenge
O(1) time

"""

class Solution:
    """
    @param n: An integer
    @return: True or false

    bit manipulation: when it is the power of 2, the highest digit must be 
    1 and others must be 0's, n&(n-1) must be 0
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n<=0:
            return False
        return True if n&(n-1)==0 else False