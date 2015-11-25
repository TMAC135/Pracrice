# coding=utf-8

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.


"""

"""
Definition of ListNode

"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 

    注意拆分链表时要不断更新next值，而且不能和原来的链表想重复，即与原来的链表要脱离开。
    """
    def partition(self, head, x):
        # write your code here
        if not head:
        	return None
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        cur = head
        cur1 = dummy1
        cur2 = dummy2
        while (cur):
        	if cur.val < x:
        		cur1.next = cur
        		cur = cur.next
        		cur1 = cur1.next
        		cur1.next=None
        	else:
        		cur2.next = cur
        		cur2 = cur2.next
        		cur = cur.next
        		cur2.next = None
        cur1.next = dummy2.next
        return dummy1.next



