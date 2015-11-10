#coding=utf-8

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
The following two linked lists:

A:          a1 → a2
				   ↘
					 c1 → c2 → c3
				   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Note
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.

Challenge
Your code should preferably run in O(n) time and use only O(1) memory.

"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	"""

	"""
	# @param headA: the first list
	# @param headB: the second list
	# @return: a ListNode


	"""
	Brute force method,time limit exceed,
	"""
	def getIntersectionNode(self, headA, headB):
		# Write your code here
		if not headA or not headB:
			return None
# 		cur1=headA
		cur2=headB
		while cur2:
			cur1=headA
			while(cur1):
				if cur1 is cur2:
					return cur1
				cur1=cur1.next

			cur2=cur2.next
		return None

	"""
	Time complexity O(m+n);
	1. 得到2个链条的长度。

	2. 将长的链条向前移动差值（len1 - len2）

	3. 两个指针一起前进，遇到相同的即是交点，如果没找到，返回null.

	相当直观的解法。空间复杂度O(1)， 时间复杂度O(m+n)

	总结： 注意 intersection 的定义，此题定义为 intersection 后面的节点肯定是
	一样的，即：
	［22，32，1，2，3，4］
	［32，31，23，45，34，1，2，3，4］ ＝》 交点为1
	我刚开始认为第一个相同的点，即
	［22，32，1，321，42］
	［43，3，23，1，34，34，24，22］ ＝》交点为1
	这种理解是错误的，因此解法一是错的暴力。 
 	"""

	def getIntersectionNode2(self, headA, headB):
		# Write your code here
		if not headA or not headB:
			return None
		# wal through the two lists and get the length of each list
		lengthA=0
		cur=headA
		while cur:
			lengthA+=1
			cur=cur.next
		lengthB=0	
		cur=headB
		while cur:
			lengthB+=1
			cur=cur.next
		# min_list and max_list are the lists corresponding to the min length and maxlength
		if lengthB >= lengthA:
			min_list=headA
			max_list=headB
		else:
			min_list=headB
			max_list=headA			
		for _ in xrange(abs(lengthA-lengthB)):
			max_list=max_list.next
		while min_list:
			if min_list is max_list:
				return min_list
			else:
				min_list=min_list.next
				max_list=max_list.next
		return None

"""
Two pointer solution (O(n+m) running time, O(1) memory):
Maintain two pointers pA and pB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6),
pB would reach the end of the merged list first, because pB traverses exactly 2 nodes less than pA does. By redirecting pB to head A, and pA to head B, we now ask pB to travel exactly 2 more nodes than pA would. 
So in the second iteration, they are guaranteed to reach the intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. So when pA/pB reaches the end of a list, record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no intersections.

1 public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
 2         if (headA == null || headB == null) {
 3             return null;
 4         }
 5         
 6         ListNode pA = headA;
 7         ListNode pB = headB;
 8         
 9         ListNode tailA = null;
10         ListNode tailB = null;
11         
12         while (true) {
13             if (pA == null) {
14                 pA = headB;
15             }
16             
17             if (pB == null) {
18                 pB = headA;
19             }
20             
21             if (pA.next == null) {
22                 tailA = pA;
23             }
24             
25             if (pB.next == null) {
26                 tailB = pB;
27             }
28             
29             //The two links have different tails. So just return null;
30             if (tailA != null && tailB != null && tailA != tailB) {
31                 return null;
32             }
33             
34             if (pA == pB) {
35                 return pA;
36             }
37             
38             pA = pA.next;
39             pB = pB.next;
40         }
41     }

"""






if __name__ == '__main__':
	a1=ListNode(0)
	a2=ListNode(2)
	a1.next=a2
	a3=ListNode(0)
	a2.next=a3
	b1=ListNode(0)
	b1.next=a2
	print Solution().getIntersectionNode(a1,b1).val




