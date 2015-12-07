# coding=utf-8

"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree
 in which the depth of the two subtrees of every node never differ by more than 1

Example
Given binary tree A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.

	首先要写一个计算二叉树高度的函数，二叉树的高度定义为：树为空时，高度为0。然后递归求解：树的高度 = max(左子树高度，右子树高度)+1(根节点要算上)。
	高度计算函数实现后，递归求解每个节点的左右子树的高度差，如果有大于1的，则return False。如果高度差小于等于1，则继续递归求解。
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
        	return True
        if abs(self.height(root.left)-self.height(root.right))<=1:
        	return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
        	return False
    
	"""
	compute the maximum height of the node 
	"""    
    def height(self,pnode):
    	if not pnode:
    		return 0
    	return max(self.height(pnode.left),self.height(pnode.right))+1