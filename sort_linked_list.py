# coding=utf-8

"""
Sort a linked list in O(n log n) time using constant space complexity

Example
Given 1-3->2->null, sort it to 1->2->3->null.
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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    这题有几个重要的点：
    	1:排序的对象是链表，不能随意得到链表中的节点，要得到中间的节点，可以使用slow and fast 指针来遍历链表
    	2:time complexity是O(nlogn),只剩下堆排序，快速排序，归并排序
    	3：space complexity 是O(1), 排除堆排序，快速排序和归并排序满足
    	4:操作链表只能通过指针，与数组操作不太一样，为了in place 排序，需要在divide 的时候将两个链表分开，
    	然后merge的时候再重新连上。每次只要返回头节点即可。
    """
    def sortList(self, head):
        # write your code here
        if not head:
        	return None
        if not head.next:
        	return head
        midNode = self.findmiddle(head)
        rightlist = self.sortList(midNode.next)
        # break the list,very important, will connect when we merge
        midNode.next = None
        leftlist = self.sortList(head)
        return self.merge(leftlist,rightlist)

    def findmiddle(self,head):
    	slow = head
    	if head.next:
    		fast = head.next
    	else:
    		return slow
    	while fast and fast.next:
    		slow = slow.next
    		fast = fast.next.next
    	return slow

    def merge(self,leftlist,rightlist):
    	dummy = ListNode(0)
    	# dummyright = ListNode(0)
    	cur_left = leftlist
    	cur_right = rightlist
    	cur = dummy
    	while cur_left and cur_right:
    		if cur_left.val < cur_right.val:
    			cur.next = cur_left
    			cur_left = cur_left.next
    		else:
    			cur.next = cur_right
    			cur_right = cur_right.next
    		cur = cur.next
    	cur.next = cur_left if cur_left else cur_right

    	return dummy.next


if __name__ == '__main__':
	a = ListNode(0)
	a.next =ListNode(5)
	a.next.next = ListNode(3)
	head = Solution().sortList(a)
	while head:
		print head.val
		head = head.next

