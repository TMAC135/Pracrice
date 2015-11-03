"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.
For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time

"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer

    This is the modified binary search, usually the binary serach is 
    based on the sorted array, but this problem is a modified version since
    we rotate the sorted array.
    Good reference:
    http://www.cnblogs.com/lichen782/p/leetcode_Search_in_Rotated_Sorted_Array.html


    """
    def search(self, A, target):
        left = 0; 
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if target == A[mid]:
                return mid
            if A[mid] >= A[left]:
                if target < A[mid] and target >= A[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[right]:
                if target > A[mid] and target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



    # use the index method of the list:
    def search2(self, A, target):
        # write your code here
        try:
            m=A.index(target)
        except ValueError:
            return -1
        return m



if __name__=='__main__':
	print Solution().search([4,5,1,2,3],6)





