# coding=utf-8

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index

Example
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

Note
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).

The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. 
This is just to let you learn how to use this problem in dynamic programming ways. 
If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    """
    Method of DP, time complexity is O(n^2),use O(n) extra space


    """
    def canJump(self, A):
        # write your code here
        if not A or A[0] == 0:
        	return False
        A_list=[0]*len(A)
        A_list[0]=1
        for i in xrange(1,len(A)):
        	for j in xrange(len(A_list[:i])):
        		if A_list[j] and A[j] >= (i-j):
        			A_list[i]=1
        			break
        return True if A_list[-1] == 1 else False


    """
    Method of greedy

    Greedy choice, if just keep track of the maxmum step we can track at the 
    current node, then we don't need extra space since we only keep trak of the
    step and we just need to pass the list once.

    Very smart method, copy from others.
    """

    def canJump2(self,A):
    	if not A:
    		return False
    	step=A[0]
    	for i in xrange(1,len(A)):
    		if step > 0:
    			step -= 1
    			step=max(step,A[i])
    			# we can judge the step size here to return the value
    			if step >= (len(A)-1-i):
    				return True
    		else:
    			return False
    	return True


if __name__ == '__main__':
	print Solution().canJump2([1,0,0])
