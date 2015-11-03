# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# example: [1,3,5,6], 5 -2
# [1,3,5,6], 2 - 1
# [1,3,5,6], 7 - 4
# [1,3,5,6], 0 - 0


# this is the typical binary search, to analyse different cases, we need to narrow down the 
# 	the search region.
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
        	return 0
        s = 0
        e=len(A)-1
        while (s < e):
        	m = (s+e)/2
        	if A[m]==target:
        		return m
        	elif A[m]>target:
        		e=m
        	else:
        		s=m+1
        return s if A[s]>=target else s+1
if __name__=='__main__':
	a=Solution()
	test=[1,3,5,6]
	value=[5,2,7,0]
	for i in value:
		print a.searchInsert(test,i)

