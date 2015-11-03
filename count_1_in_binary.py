# Count how many 1 in binary representation of a 32-bit integer.

# example: given 32,return 1

# challenge: O(m) time with m is number of 1's for the number.

class Solution:

	"""
	since it have the limit of the time O(m), usually we will do it in the ]
	bit manipulation, we continue shift the number to the right and count 
	the 1's in the last bit.
	But we still need to be careful with negative number
	"""

    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count=0
        for _ in xrange(32):
            count+=(num&1)
            num=(num>>1)
        return count