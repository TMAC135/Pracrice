# Given a binary tree, return the inorder traversal of its nodes' values.

# Challenge: Can you do it without recursion?

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
class Solution1(object):
	"""
	@param root: The root of binary tree.
	@return: Inorder in ArrayList which contains node values.
	"""
	def inorderTraversal(self, root):
		# write your code here
		if not root:
			return []
		res=[]
		self.recursion(root,res)
		return res

	def recursion(self,root,res):																																																																																																																																																																																																																															
		if root:
			self.recursion(root.left,res)
			res.append(root.val)
			self.recursion(root.right,res)


#  Method without recursion,using a stack to store the data
class Solution2(object):
	"""
	the difficulty here is how to judge our traversal is finished. The stack has 
	stored the nodes that we haven't added to our final result, however, the empty 
	stack doesn't necessarily mean we are done. we still need to check the right node and 
	add them into the stack if they are not empty. Thus we need to update the next node in the
	while loop, that's key of solving this problem with stack.

	main reference: http://www.cnblogs.com/zuoyuan/p/3720273.html 

	"""
	def inorderTraversal(self, root):
		L=[]
		stack = []
		while root or stack:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				L.append(root.val)
				root = root.right
		return L



if __name__=='__main__':
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	a.right=b
	b.left=c
	print Solution2().inorderTraversal(a)









