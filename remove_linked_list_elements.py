# Remove all elements from a linked list of integers that have value val

# example: Given 1->2->3->3->4->5->3, val = 3
# return the list 1->2->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
    	"""
    	it is an easy problem, but we need to be careful when we pass 
    	the list. 
    	In my code, I have always been sure that the cur node is not the
    	node we want to delete, thus we need to check the head node firstly 
    	and then pass the linked node.
    	"""
        # Write your code here
        if not head:
            return None
        while(head.val==val):
            if head.next!=None:
                head=head.next
            else:
                return head.next
        cur = head
        while (cur.next!=None):
            if cur.next.val == val: 
                tmp=cur.next
                cur.next=tmp.next
            else:
                cur = cur.next
        return head