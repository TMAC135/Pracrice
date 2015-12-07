# coding=utf-8
"""
Given a binary search tree and a new tree node, insert the node into
 the tree. You should keep the tree still be a valid binary search tree.

Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6

Challenge
Can you do it without recursion?
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
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.

    插入的节点的子树肯定有 null 的，这是判断循环结束的条件
    """
    # recursion way
    def insertNode(self, root, node):
        # write your code here
        if not root:
            return node
        if root.val > node.val:
            root.left=self.insertNode(root.left,node)
        else:
            root.right=self.insertNode(root.right,node)
        return root


    # non recursion way
    def insertNode2(self, root, node):
    	if not root:
    		return node
    	if not node:
    		return root
    	cur = root
    	while cur:
    		if cur.val > node.val and not cur.left:
    			cur.left = node
    			break
    		elif cur.val < node.val and not cur.right:
    			cur.right = node
    			break
    		elif cur.val > node.val:
    			cur = cur.left
    		else:
    			cur=cur.right
    	return root




