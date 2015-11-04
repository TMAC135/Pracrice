
 #coding=utf-8 

"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

Example
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
	\       /     /      / \      \
	 3     2     1      1   3      2
	/     /       \                 \
   2     1         2                 3


"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

class Solution:
	# @return a list of tree node
	"""
	if we want to return the number of BST, DP is sufficient enough
	but if we want to enumerate all BSTs, we need to use dfs to traversal the 
	tree and gives us the all structuraled trees.

	"""
	def dfs(self, start, end):
		if start > end: return [None]
		res = []
		for rootval in range(start, end+1):　			
		#rootval为根节点的值，从start遍历到end
			LeftTree = self.dfs(start, rootval-1)
			RightTree = self.dfs(rootval+1, end)
			for i in LeftTree:　　　　　　　　　　　　　　　　#i遍历符合条件的左子树
				for j in RightTree:　　　　　　　　　　　　  #j遍历符合条件的右子树
					root = TreeNode(rootval)
					root.left = i
					root.right = j
					res.append(root)
		return res
	def generateTrees(self, n):
		return self.dfs(1, n)



if __name__=='__main__':
	print Solution().generateTrees(3)