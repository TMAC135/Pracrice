# coding=utf-8
"""
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.
A valid path is from root node to any of the leaf nodes

Given a binary tree, and target = 5:

	 1
	/ \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]

"""

"""
Definition of TreeNode:

"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class Solution:
	# @param {TreeNode} root the root of binary tree
	# @param {int} target an integer
	# @return {int[][]} all valid paths
	"""
	注意递归时用list 要小心sharing reference
	"""
	def binaryTreePathSum(self, root, target):
		# Write your code here

		"""
		first version, not working.
		"""
		# if not root:
		# 	return []
		# stack = [root]#using stack to travel the tree,dfs
		# hashSet = dict([(target-root.val,[root.val])])
		# res = [] 
		# while stack:
		# 	if not hashSet:
		# 		break
		# 	tmp = stack.pop()
		# 	if not tmp.left:
		# 		stack.append(tmp.left)
		# 	if not tmp.right:
		# 		stack.append(tmp.right)
		# 	if tmp is not root:
		   #  	if tmp.val not in hashSet:
		   #  		keys = hashSet.keys()
		   #  		values = hashSet.values()
		   #  		for i in xrange(len(keys)):
		   #  			keys[i] -= tmp.val
		   #  			values[i].append(tmp.val)
		   #  		hashSet = dict([(keys[i],values[i]) for i in xrange(len(keys))]) 
		   #  	else:
		   #  		res.append(hashSet(tmp.val))
		"""
		using recursion method
		"""
		hashSet = {target:[]}
		res = []

		self.recursion(root,hashSet,target,res)

		return res

	def recursion(self,node,hashSet,target,res):
		if node:
				# return
			keys = hashSet.keys()[0]
			values = hashSet.values()[0]
			keys -= node.val
			values_tmp = values[:] + [node.val]#need to have a shollow copy of list!!!!Otherwise we manipulate the same list
			tmp = {keys:values_tmp}
			if keys == 0:
				res.append(values_tmp)
			self.recursion(node.left,tmp,target,res)
			self.recursion(node.right,tmp,target,res)

	"""
	可以不用字典，相应的我们传递到达每个节点的sum值和相应的valuelist即可,
	例如如下：
	"""
	def pathSum(self, root, target):
		"""
		others
		"""
		# def dfs(root, currsum, valuelist):
		# 	if root.left==None and root.right==None:
		# 		if currsum==sum: res.append(valuelist)
		# 	if root.left:
		# 		dfs(root.left, currsum+root.left.val, valuelist+[root.left.val])
		# 	if root.right:
		# 		dfs(root.right, currsum+root.right.val, valuelist+[root.right.val])
		
		# res=[]
		# if root==None: return []
		# dfs(root, root.val, [root.val])
		"""
		my version
		"""
		def dfs(node,cursum,valuelist):
			if node:
				cursum += node.val
				if cursum == target:
					res.append(valuelist+[node.val])
				else:
					dfs(node.left,cursum, valuelist+[node.val])
					dfs(node.right,cursum, valuelist+[node.val])
		res = []
		dfs(root,0,[])
		return res




if __name__ == '__main__':
	root = TreeNode(1);
	a=TreeNode(2);
	b=TreeNode(4);
	c=TreeNode(2);
	d=TreeNode(3);
	root.left = a
	root.right = b
	a.left = c
	a.right = d
	print Solution().binaryTreePathSum(root,5)
	print Solution().pathSum(root,5)


					




