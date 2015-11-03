# Suppose a sorted array is rotated at some pivot unknown to
# you beforehand.(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.

# example: given [4,5,6,7,0,1,2], return 0


class Solution:
	"""
	(1) since the test data is pretty simple, just return min(num)
	can pass the OJ
	(2) using binary search to find the minimum, since we already know the 
	the rotated array is from the sorted array, then we can make sure 
	the num[low] > num[high],otherwise just return num[low]
	(3) keep the property of (2) and we can finally have two elements,
	low and high, and just return high. Notice the discriminent of 
	the while loop - (low<high-1) since we finally have 2 elements.
	"""
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if not num:
        	return None
        low=0
        high=len(num)-1
        if num[low]<num[high]:
        	return num[low]
        while low<high-1:
        	mid=(low+high)/2
        	if num[mid]>num[high]:
        		low = mid
        	else:
        		high = mid 
        return num[high]