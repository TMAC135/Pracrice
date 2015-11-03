# Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

# Example: Given [1,2,2,3,4,4,5,3] return 1 and 5

# challenge: O(n) time and 0(1) extra space


# Main idea:Trying to partioning into 2 group where each group only contains 1 unique number.
class Solution:
    def singleNumberIII(self, A):
        """
        Bit manipulation
        If two numbers are different, \exists 1 bit set in one while unset in the other.
        To get the rightmost set bit: n&(~n+1), which is equivalent to n&-n (2's complement)
        :param A: An integer array
        :return: Two integer

        main reference : http://blog.xiaohuahua.org/2015/01/22/lintcode-single-number-iii/
        """
        bits = 0
        # first pass, we get final answer x^y
        for a in A:
            bits ^= a
        # rightmost means the least significant bit that differs from the x and y.
        # 	this will be our test criteria for the original list. we will use it to
        # 	to partition the original group into 2 groups and each group will contain one 
        # 	answer. Then for each group, the problem to find the unique number is the same as
        # 	singlenumberI.
        rightmost_set_bit = bits&-bits # this is a little tricky, we will return the value 
 # where only one bit is 1 and others are all 0's.The meaning behind this is that the bit which is 
 # 1 indicate the first 1 in the x^y, and also means the first bit where x and x are different, 
 # this bit is sufficient to test x,y are different.

        bits1 = 0
        bits2 = 0
        for a in A:
            if a&rightmost_set_bit:
                bits1 ^= a
            else:
                bits2 ^= a

        return bits1, bits2

if __name__=='__main__':
	print Solution().singleNumberIII([1,2,2,3,4,4,5,3])
