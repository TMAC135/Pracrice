"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

Example:
Given binary tree {3,9,20,#,#,15,7},
   3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

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
    @return: buttom-up level order in a list of lists of integers

    same idea as the binary_tree_level_order_traversal.py we just need
    to return the reverse order of the previous version
    """
    def levelOrderBottom(self, root):
        # write your code here
                # write your code here
        if not root:
            return []
        res=[]
        queue=[root]
        while (queue):
        	tmp=[]
            # we need to get the length of current level and then add more
            # nodes in this queue
        	length=len(queue)
        	for i in xrange(length):
        		pop=queue.pop(0)
        		tmp.append(pop.val)
        		self.Queue(pop,queue)
        	res.append(tmp)
        return res[::-1]

    def Queue(self,node,queue):
    	if node.left:
    		queue.append(node.left)
    	if node.right:
    		queue.append(node.right)