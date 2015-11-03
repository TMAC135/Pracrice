# Given a m x n grid filled with non-negative numbers,
 # find a path from top left to bottom right which minimizes
  # the sum of all numbers along its path.


# here i use only use the O(min(row,column)) extra space
class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    here if we use the matrix to store the result, the space complexity is 
    O(m*n),which could be time cost.
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid:
        	return 0
        row=len(grid)
        column=len(grid[0])
        if row==1:
        	return sum(grid[0])
        elif column==1:
        	res = 0
        	for i in xrange(row):
        		res+=grid[i][0]
        	return res

        # initialization for the first prev
        prev=[0 for _ in range(column-1)]
        prev[0]=grid[0][0]+grid[0][1]
        for i in xrange(2,column):
        	prev[i-1]=prev[i-2]+grid[0][i]
        # return prev
        d=[0 for _ in range(column-1)]
        start=grid[0][0]

        for i in xrange(1,row):
        	start=grid[i][0]+start
        	cur=start
        	for j in xrange(1,column):
        		d[j-1]=min(prev[j-1],cur)+grid[i][j]
        		cur=d[j-1]
        	prev=d[:]

        return d

if __name__=='__main__':
	test=[[1,3,1],[1,5,1],[4,2,1]]
	print Solution().minPathSum(test)
