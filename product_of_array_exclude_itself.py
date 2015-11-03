"""
Given an integers array A.
Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example:
For A = [1, 2, 3], return [6, 3, 2].


"""


class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        if not A:
        	return []
        if len(A)==1:
        	return [1]
        res=[]
        for i in xrange(len(A)):
        	tmp=A[:]#shollow copy of original list
        	tmp.remove(tmp[i])
        	res.append(self.product(tmp))
        return res

    def product(self,A):
    	res=1
    	for i in A:
    		res*=i
    	return res

if __name__=='__main__':
	print Solution().productExcludeItself([1,2,3]) 
