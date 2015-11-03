"""
Merge two sorted (ascending) linked lists and return it as 
a new sorted list. The new sorted list should be made by splicing 
together the nodes of the two lists and sorted in ascending order

Example: 
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.

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
    @param two ListNodes
    @return a ListNode

    Notice that to judge the first version I use is to judge the first head and 
    then retuen the head finally, and I also check whether l1 and l2 are None
    individually, it is kind of redundant and we can judge them in the while loop.
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here

        # if not l1:
        # 	return l2
        # if not l1:
        # 	return l2
       	# this is kind of redundant since we will compare in the while loop
        # if l1.val<=l2.val:
        # 	head=l1
        # 	l1=l1.next
        # else:
        # 	head = l2
        # 	l2=l2.next

        # we can use a fake head, the true head is actually the next value of the fake head
        fakehead=ListNode(0)
        prev=fakehead
        while(l1 and l2):
        	if l1.val<=l2.val:
        		prev.next=l1
        		l1=l1.next
        	else:
        		prev.next=l2
        		l2=l2.next
        	prev=prev.next
        if not l1:
        	prev.next=l2
        elif not l2:
        	prev.next=l1
        return fakehead.next


if __name__=='__main__':
	a=ListNode(1)
	b=ListNode(8)
	c=ListNode(11)
	a.next=b
	b.next=c
	A=ListNode(2)
	head=Solution().mergeTwoLists(a,A)
	while(head):
		print head.val
		head=head.next





