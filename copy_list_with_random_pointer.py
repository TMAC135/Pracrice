"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.
Return a deep copy of the list

Challenge:
solve it with O(1) space


"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None
class Solution:
	# @param head: A RandomListNode
	# @return: A RandomListNode

	"""
	method 1: not a good choice
	first method i come up with, time limit exceed and also the
	space complexity is O(n) since we store our node information in the 
	dictionary, which is not a good idea. 
	"""
	"""
	def copyRandomList(self, head):
		# write your code here
		if not head:
			return None
		fakehead=RandomListNode(0)
		cur=fakehead
		ite=head
		d={}
		while(ite):
			tmp=RandomListNode(ite.label)
			if ite.random:
				if ite.random.label not in d:
					tmp.random=RandomListNode(ite.random.label)
					d[ite.random.label]=tmp.random
				else:
					tmp.random=d[ite.random.label]
			else:
				tmp.random=None
			if ite.next:
				if ite.next.label not in d:
					tmp.next=RandomListNode(ite.next.label)
					d[ite.next.label]=tmp.next
				else:
					tmp.next=d[ite.next.label]

			ite=ite.next
			cur.next=tmp
			cur=cur.next
		return fakehead.next
		"""


	"""
	method by others, 
	reference: http://www.cnblogs.com/zuoyuan/p/3745126.html
	firstly construt a new list which is just insert the node which is exactly the same as previous one
	then we will pass the new list and delete the repeated node from the new list. 

	"""
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		if head == None: return None
		tmp = head
		while tmp:
			newNode = RandomListNode(tmp.label)
			newNode.next = tmp.next
			tmp.next = newNode
			tmp = tmp.next.next
		tmp = head
		while tmp:
			if tmp.random:
				tmp.next.random = tmp.random.next
			tmp = tmp.next.next
		newhead = head.next
		pold = head
		pnew = newhead
		while pnew.next:
			pold.next = pnew.next
			pold = pold.next
			pnew.next = pold.next
			pnew = pnew.next
		pold.next = None
		pnew.next = None
		return newhead

