# Given preorder and inorder traversal of a tree, construct the binary tree

# example in-order [1,2,3], pre-order [2,1,3],return a tree.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node

    """
    this is a good example to use the recursion in the tree. Usually, using 
    recursion problem to solve the tree problem is a option. 
    but we need to make sure every recursion step will be subset of previous
    problem and moreover the base case should be right. 

    similar problem use postorder and inorder.
    """
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : index + 1], inorder[0 : index])
        root.right = self.buildTree(preorder[index + 1 : len(preorder)], inorder[index + 1 : len(inorder)])
        return root

