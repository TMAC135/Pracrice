"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].



"""

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if not A:
        	return 0
        res=1
        cur=A[0]
        # this is the version where we don't change the original array which is A
        # but the problem do need us to remove the duplicated elements thus we need to 
        # pop out these duplicated elements
        # for i in xrange(1,len(A)):
        # 	if A[i]!=cur:
        #   		res+=1
        #   		cur=A[i]
        # this is the version with removement for the dupliacation
        i=1
        for _ in xrange(1,len(A)):
        	if A[i]!=cur:
        		# be careful about the arrangement of these three lines, otherwise
        		# we will get list out of indeces.
          		res+=1
          		cur=A[i]
          		i+=1
          	else:
          		A.remove(A[i])

        return res

if __name__=='__main__':
	print Solution().removeDuplicates([1,1,2])
