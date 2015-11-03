# import numpy as np

# class Solution(object):
# 	def numIslands(self, grid):
# 		#those two lines extract the length of row and columns in the grid
# 		row = len(grid[:,0])
# 		column = len(grid[0,:])
		
# 		#we add extral column and row which is 0, not affecting the final results
# 		extra_col=np.zeros([row,1])
# 		extral_row=np.zeros([1,column+1])
# 		grid=np.hstack((grid,extra_col))
# 		grid=np.vstack((grid,extral_row))
# 		count=0
# 		for cindex in xrange(column):
# 			for aindex in xrange(row):
# 				if grid[(aindex,cindex)]==1:
# 					count+=1
# 					if grid[(aindex+1,cindex)]==1 or grid[(aindex,cindex+1)]==1:
# 						count-=1
# 					# elif grid[(aindex,cindex+1)]==1:
# 						# count-=1
# 		return count

# class Solution:
#     # @param {boolean[][]} grid a boolean 2D matrix
#     # @return {int} an integer
#     def numIslands(self, grid):
#         # Write your code here
#         if not grid:
#         	return 0
#         for list in grid:
#         	list.append(0)
#         grid.extend([[0 for _ in range(len(grid[0]))]])
#         count=0
#         rep=0
#         for i in range(len(grid)-1):
#         	for j in range(len(grid[i])-1):
#         		if grid[i][j] == 1:
#         			count += 1
#         			if grid[i+1][j] == 1:
#         				rep += 1
#         			if grid[i][j+1] == 1:
#         				rep +=1
#         return count-rep

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid:
        	return 0
        for list in grid:
        	list.append(0)
        grid.extend([[0 for _ in range(len(grid[0]))]])
        count=0
        for i in range(len(grid)-2,-1,-1):
        	for j in range(len(grid[i])-2,-1,-1):
        		if grid[i][j] == 1:
        			count += 1
        			if grid[i+1][j] == 1 or grid[i][j+1]==1:
        				count -= 1
        return count
        				



