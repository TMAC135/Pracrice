# Given a linked list, swap every two adjacent nodes and return its head.

# Example 1->2->3->4, return the list as 2->1->4->3

# 	challenge: using constant space.You may not modify the values
# in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    # @param head, a ListNode
    # @return a ListNode
    """
    be careful when we swap the nodes in the linked list,we should 
    restore the original linking status
    """

    def swapPairs(self, head):
        # Write your code here
        if not head:
        	return None
        cur=head

        if head.next:
            head=head.next
            prev=ListNode(0)
            while(cur):
            	if cur.next:
    	        	next=cur.next
    	        	prev.next,cur=self.swap(cur,next)
    	        	prev=cur
    	        	cur=cur.next
    	        else:
    	        	break
        return head


# given the 2 nodes which is in order node1->node2,
# we swap the node such that the order is node2->node1 and return node2
    def swap(self,node1,node2):
    	tmp = node2.next
    	node2.next=node1
    	node1.next=tmp
    	return (node2,node1)

# to test the different cases, we need to count noth the even and odd
# numbers of the nodes, be careful about the judge equation for the while loop 
if __name__=='__main__':
	a,b,c,d,e=ListNode(1),ListNode(2),ListNode(3),ListNode(4),ListNode(5)
	a.next=b
	b.next=c
	c.next=d
	d.next=e
	head=Solution().swapPairs(a)
	while(head):
		print head.val
		head=head.next











