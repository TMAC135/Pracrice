# You have two numbers represented by a linked list, 
	# where each node contains a single digit. 
	# The digits are stored in reverse order, such that the 1's digit
 	# is at the head of the list. Write a function that adds the two numbers
 	# and returns the sum as a linked list.

# Given 7->1->6 + 5->9->2. That is, 617 + 295.

# Return 2->1->9. That is 912.

# Given 3->1->5 and 5->9->2, return 8->0->8.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# code from others, since it's a singled linked list, we can add a head 
# 	like dummy=ListNode(0), and append all our results finally return the 
#	dummy.next which is essentially the real head of the final result.
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0); p = dummy
        # compare the length of l1 and l2, this is the common length
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next; l2 = l2.next; p = p.next
        # if l2 is longer
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next; p = p.next
        # if l1 is longer
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next; p = p.next
        # flag is important since we may have wrong answer like 9999+11
        if flag == 1: p.next = ListNode(1)
        return dummy.next

