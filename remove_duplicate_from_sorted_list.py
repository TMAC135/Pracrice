# coding=utf-8
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
	@param head: A ListNode
	@return: A ListNode
	"""
	"""
	this version is time limit exceed 
	"""
	def deleteDuplicates(self, head):
		# write your code here
		if not head:
			return head
		cur = head
		value = []
		prev = ListNode(0)#dummy node
		while cur:
			if cur.val not in value:
				value.append(cur.val)
				prev.next = cur
				prev = prev.next
				cur = cur.next
				prev.next = None
			else:
				cur = cur.next

		return head
	"""
	notoce that it is a sorted linked list,we don't need a list to store all
	the information, we can only track one value at a time.
	"""

	def deleteDuplicates2(self, head):
		# write your code here
		if not head:
			return head
		cur_value = 'junk'
		cur = head
		prev = ListNode(0)#dummy node
		while cur:
			if cur.val != cur_value:
				cur_value = cur.val
				prev.next = cur
				prev = prev.next
				cur = cur.next
				prev.next = None
			else:
				cur = cur.next
		return head



