# Write an efficient algorithm that searches for a value in
# an m x n matrix, return the occurrence of it.
# This matrix has the following properties:
# 	* Integers in each row are sorted from left to right.
# 	* Integers in each column are sorted from up to bottom.
# 	* No duplicate integers in each row or column.


# Challenge: O(m+n) time and O(1) extra space

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix

    	For this problem, I didn't come up with this O(m+n) method. It is very tricky and impressive.
    Remember that we are given the sorted array for the rows and columns, this is important information.
    We are starting from the right top of the matrix (or left bottom is the same idea), once we find target 
    value is bigger than the current state, we are confident that this row don't have the target, we need to move 
    to the next row, similarly, if we find the target value is less than the current state, we are confident that 
    the column in the current stata doesn't have target, we need to move left. 
    The smartness of this idea to get rid of redundent comparison since we already have the sorted row and comlumn.
    But to come up with this search is a difficuilt process,and this is the key of this problem.


    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0
        row=len(matrix)
        column=len(matrix[0])
        res=0
        i=0
        j=column-1
        while(i<row and j>=0):
            if matrix[i][j] == target:
                res+=1
                i+=1
                j-=1
            elif matrix[i][j] > target:
                j-=1
            else:
                i+=1
        return res
		