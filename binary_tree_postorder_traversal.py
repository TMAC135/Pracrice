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
	def postorderTraversal(self, root):
		# write your code here
		if not root:
			return []
		res=[]
		self.recursion(root,res)
		return res

	def recursion(self,root,res):
		if root:
			self.recursion(root.left,res)
			self.recursion(root.right,res)
			res.append(root.val)

# without recursion, 1 stack,space complexity O(h) where h is heitht of the binary tree.
class Solution2(object):
	"""The postorder traversal without recursion is the most difficult one comparing with
	the others. By intuition, we need to traversal the tree from bottom to top, which is just the 
	reverse of the preorder? but how to implement it in the stack? Well, we need to be very careful 
	when we dicide when to push the item or pop the item from the stack. 
	The trick here is using a label called prev to mark the previous item we have just poped, if previous 
	item happened to be the kid node of the current node, which means we don't have any right nodes at 
	current node, we are safe to pop out the item. Notice that the first prev item must be the left 
	most item in the tree, otherwise we can't pop out item since we need to obey the output rule:
	left->right->parent, we set the pre as None untill we find the left most item.

	main reference:
	http://www.cnblogs.com/zuoyuan/p/3720846.html  : which is clear and easy to understand.

	"""
	def postorderTraversal(self, root):
		list=[]
		stack = []
		pre = None
		if root:
			stack.append(root)
			while stack:
				curr = stack[-1]
				# this criteria is the key of the this method, the former one tell us 
				# 	the current nodes don't have kids, the latter tells us the previous node
				#	is the kid of current node, which means we don't have right nodes for the 
				#	current node.
				#	Either one of 2 cases satisfies, we are safe to pop out items
				# 	otherwise, we need keeping pushing items into stack.
				if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
					list.append(curr.val)
					stack.pop()
					pre = curr
				# we keep pushing  nodes into the stack, since we don't satisfy the criteria we
				# 	set before,
				else:
					if curr.right: stack.append(curr.right)
					if curr.left: stack.append(curr.left)
		return list

# Without Recursion, using 2 stack, space complexity O(n)
class Solution3(object):
	"""
		http://bookshadow.com/weblog/2015/01/19/binary-tree-post-order-traversal/ 
		Also provide a method using double-stack, anylysis the space complexity between two methods.

		http://bookshadow.com/weblog/2015/01/19/leetcode-binary-tree-postorder-traversal/
		implement in python


		My first thought for this problem is similar to this, however, I didn't come out with 
		using another stack. Actually, one of stack will store  the final traversal order of 
		the node while the other keep track of the kids from current node. Two stacks work together
		just acting like the reverse of preorder traversal

	"""
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ans[::-1]


		


if __name__=='__main__':
	a=TreeNode(1)
	b=TreeNode(2)
	c=TreeNode(3)
	a.right=b
	b.left=c
	print Solution2().postorderTraversal(a)