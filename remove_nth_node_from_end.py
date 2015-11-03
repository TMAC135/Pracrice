"""
Given a linked list, remove the nth node from the end of list and return its head.

example: 
Given linked list: 1->2->3->4->5->null, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5->null.

challenge: O(n) time
"""


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if not head:
        	return None
        tmp=head
        for _ in xrange(n-1):
        	tmp=tmp.next
        # first fake head
        fakehead=ListNode(0)
        fakehead.next=head
        prev=fakehead
        while tmp.next:
        	tmp=tmp.next
        	# prev=prev.next
        	prev=prev.next
        prev.next=prev.next.next
        return fakehead.next
"""
code from others, the same idea as me, but seems more clear, dummy is the
fakehead and p1 anf p2 are two pointers we pass through the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:
            p1=p1.next; p2=p2.next
        p2.next=p2.next.next
        return dummy.next
"""






