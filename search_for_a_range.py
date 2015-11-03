"""
Given a sorted array of n integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4]

Challenge
O(log n) time

"""

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]

    if we have the duplicated element in the sorted array, we may as well 
    to use 2 while loop and to find the left node and right nodes seperatly
    which also in the O(log(n)) time complexity.
    """

    """ Method1:
    when we hit the target, we are not done since there is a possibility 
    we have duplicated element.
    Method 1 is to pass down the left range and right range, but the problem 
    here is when the array is big and the element is all the same, thus 
    the complecity is O(n) instead of O(logn).

    """
    def searchRange(self, A, target):
        left = 0; 
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                list = [0, 0]
                if A[left] == target: list[0] = left
                if A[right] == target: list[1] = right
                for i in range(mid, right+1):
                    if A[i] != target: list[1] = i - 1; break
                for i in range(mid, left-1, -1):
                    if A[i] != target: list[0] = i + 1; break
                return list
        return [-1, -1]


    """ Method2:
    this method guarantee we have time complexity O(logn).
    Firstly we search the left node and then based on this left node, we 
    find the right node. The differences of these two is just where we put
    the equal sigh we compare the mid node with start and end nodes.


    """
    def searchRange2(self, A, target):
        solution =[-1,-1];
        start = 0
        end = len(A)-1
        while start<end:
            midpoint = (start + end )/2
            # first case, we find the target,then we ignore the 
            # right range since we firstly need to find the left 
            # node.
            if A[midpoint] == target:
                end = midpoint
            elif A[midpoint] < target:
                start = midpoint+1
            else:
                end = midpoint -1
        # this is the case we don't have target value in the array
        # thus we can just return [-1,-1]
        if A[start]!= target:
            return solution
        # then given the left node, we try to find the right node
        solution[0] = start
        end = len(A)-1
        while start<end:
            midpoint = (start + end +1)/2
            # ignore the left range
            if A[midpoint] == target:
                start = midpoint
            else:
                end = midpoint -1
        solution[1] = start
        return solution


if __name__=='__main__':

	print Solution().searchRange2([1,2,2,3,4,5,6],7)
