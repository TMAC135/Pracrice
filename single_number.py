# Given 2*n + 1 numbers, every numbers occurs twice except one, find it

# example: Given [1,2,2,1,3,4,3], return 4

# Challenge: one pass, constant extra sapce

class Solution:
    """
    @param A : an integer array
    @return : a integer
    This is a problem about the bit manipulation using xor
    for any number x, x^0=x,x^x=0,then y^x^x=y
    """
    def singleNumber(self, A):
        # write your code here
        if not A:
        	return 0
        ans=A[0]
        for  i in xrange(1,len(A)):
        	ans^=A[i]
        return ans

if __name__ == '__main__':
	print Solution().singleNumber([1,2,2,1,3,4,3])