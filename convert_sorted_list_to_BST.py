# coding=utf-8

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

               2
1->2->3  =>   / \
             1   3
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node

    total runtime for this case is 1557ms, which is pretty large,
    better to have a solution without recursion

    """
    def sortedListToBST(self, head):
        # write your code here
        if not head:
        	return None
        cur = head
        val = [head.val]#store the value in a list
        while cur.next:
        	val.append(cur.next.val)
        	cur =cur.next
        root = self.build(val)
        return root

    def build(self,val):
    	if not val:
    		return None
    	mid = len(val)/2
    	cur = TreeNode( val[mid] )
    	cur.left = self.build(val[:mid])
    	cur.right = self.build(val[mid+1:])
    	return cur










