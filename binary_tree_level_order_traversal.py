"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level)

Example:
Given binary tree {3,9,20,#,#,15,7}:
  3
   / \
  9  20
    /  \
   15   7
return it's level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Challenge:
Challenge 1: Using only 1 queue to implement it.
Challenge 2: Use DFS algorithm to do it.


"""

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers

    this is method of BFS, we use one queue to store the current level 
    information. The key for this method is how to keep tracking of a 
    level using only one queue.

    how about using DFS?
    """
    def levelOrder(self, root):
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
        return res


    def Queue(self,node,queue):
    	if node.left:
    		queue.append(node.left)
    	if node.right:
    		queue.append(node.right)

if __name__=='__main__':
	a1=TreeNode(3)
	a2=TreeNode(9)
	a3=TreeNode(20)
	a4=TreeNode(15)
	a5=TreeNode(7)
	a1.left=a2
	a1.right=a3
	a3.left=a4
	a3.right=a5

	print Solution().levelOrder(a1)

        	

