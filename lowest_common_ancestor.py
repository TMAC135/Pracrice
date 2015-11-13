# coding=utf-8

"""
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7

"""

"""
Definition of TreeNode:
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None

import copy
class Solution:
	"""
	@param root: The root of the binary search tree.
	@param A and B: two nodes in a Binary.
	@return: Return the least common ancestor(LCA) of the two nodes.

	My thoughts:
	I firstly walk through the tree and find these 2 nodes from the root, and I use 2 lists 
	to store the nodes in the paths. Thus given these 2 lists' information, we just compare the 
	the information and return the same nodes. Notice the right most nodes of two lists are 
	near to the node A or node B. 

	Another thing need to pay attention is I use recursion to record the information in list, 
	the id of a + [2] is different from a, which means the tmp which pass to the next recursion level 
	is safe. This is dfs basically.  
	""" 
	def lowestCommonAncestor(self, root, A, B):
		# write your code here
		if not root:
			return None
		ancestor_A=self.ancestors(A,root,[])
		# return ancestor_A #used to debug, 
		ancestor_B=self.ancestors(B,root,[])
		# return ancestor_B #used to debug
		for i in ancestor_A[::-1]:
			if i in ancestor_B:
				return i
		return None

	def ancestors(self,node,root,list):
		if root:
			if root.val != node.val:
				tmp=list+[root]
				left=self.ancestors(node,root.left,tmp)
				right=self.ancestors(node,root.right,tmp)
				return left if left else right
			else:
				return list+[root]
		else:
			return None

	"""
	method from others, 

	public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //发现目标节点则通过返回值标记该子树发现了某个目标结点
        if(root == null || root == p || root == q) return root;
        //查看左子树中是否有目标结点，没有为null
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        //查看右子树是否有目标节点，没有为null
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        //都不为空，说明做右子树都有目标结点，则公共祖先就是本身
        if(left!=null&&right!=null) return root;
        //如果发现了目标节点，则继续向上标记为该目标节点
        return left == null ? right : left;
    }
}


	"""

if __name__ == '__main__':
	a = TreeNode(4)
	b = TreeNode(3)
	c = TreeNode(7)
	d = TreeNode(5)
	e = TreeNode(6)
	a.left = b
	a.right = c 
	c.left = d
	c.right = e
	print Solution().lowestCommonAncestor(a,b,e)







