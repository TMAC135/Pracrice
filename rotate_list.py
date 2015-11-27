# coding=utf-8

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


    """
    naive method, first pass through the list and get the total length of the list,then 
    walk again to partition the list and connect the two part.
    Time limit exceed!!!
    """

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        # write your code here
        if not head:
        	return None
        cur = head
        length = 1
        while cur.next:
        	cur = cur.next
        	length += 1
        last = cur #use this last node to connect the two part in the next few steps.
        rotate_length = k % length
        """
        this is my original method, basically the same idea as below;
        """
        # if rotate_length == 0:
        # 	return head
        # cur = head
        # for _ in xrange(length-rotate_length - 1):
        # 	cur = cur.next
        # newhead = cur.next
        # cur.next = None
        # last.next = head
        # return newhead
        """ from others:
        or we can make the linked list as a circled chain so we can break this chain once we hit the condition 
        and agian seperate it as a linked list.
        """
        cur.next = head
        for _ in xrange(length - rotate_length):
        	cur = cur.next
        newhead = cur.next
        cur.next = None
        return newhead



      




