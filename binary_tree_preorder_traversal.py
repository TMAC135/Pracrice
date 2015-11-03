# Given a binary tree, return the preorder traversal of its nodes' values.

# Same requrements as inorder traversal,do it withour recursion

"""
Definition of TreeNode:
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None



# This is the method using recursion,which is pretty simple

class Solution:
	"""
	@param root: The root of binary tree.
	@return: Preorder in ArrayList which contains node values.
	"""
	def preorderTraversal(self, root):
		# write your code here
		if not root:
			return []
		res=[]
		self.recursion(root,res)
		return res

	def recursion(self,root,res):
		if root:
			res.append(root.val)
			self.recursion(root.left,res)
			self.recursion(root.right,res)

# without recursion
class Solution2(object):
	"""The intuition behind the preorder traversal is to output the values from 
	top to down, like the inorder traversal, the stack will help us to determine the end of 
	traversal,but we need to be careful when appending the nodes between right nodes and left 
	nodes, since we need to obey the rule of stack.
	"""
	def preorderTraversal(self,root):
		if not root:
			return []
		res=[]
		stack=[root]
		while stack:
			pop=stack.pop()
			res.append(pop.val)
			# we need firstly to append right node in the stack since the preorder order is 
			# 	node ,node.left,node.right, then the elements come in early will be processed 
			# 	later.
			if pop.right:
				stack.append(pop.right)
			if pop.left:
				stack.append(pop.left)
		return res

			

		


if __name__=='__main__':
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	a.right=b
	b.left=c
	print Solution2().preorderTraversal(a)