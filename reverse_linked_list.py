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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.

    The key in the problem of single linked list is that the next of the 
    current node can be only one node, thus if we assign an another next 
    for the current node, we need to have a backup for the orininal next node.
     
    """
    def reverse(self, head):
        # write your code here
        if not head:
            return None
        cur=head
        prev=None
        while(cur.next):
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        cur.next=prev
        return cur

