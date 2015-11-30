# coding=utf-8

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

Example
For example,
Given 1->2->3->4->null, reorder it to 1->4->2->3->null.



"""

"""
Definition of ListNode
"""

class ListNode(object):

	def __init__(self, val, next=None):
		self.val = val
		self.next = next

"""
copy from others, but the same logic as mine,first to break the lists into 
two parts and merge them.

"""

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head==None or head.next==None or head.next.next==None: return head
        
        # break linked list into two equal length
        slow = fast = head                              #快慢指针技巧
        while fast and fast.next:                       #需要熟练掌握
            slow = slow.next                            #链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy=ListNode(0); dummy.next=head2             #翻转前加一个头结点
        p=head2.next; head2.next=None                   #将p指向的节点一个一个插入到dummy后面
        while p:                                        #就完成了链表的翻转
            tmp=p; p=p.next                             #运行时注意去掉中文注释
            tmp.next=dummy.next
            dummy.next=tmp
        head2=dummy.next

        # merge two linked list head1 and head2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; tmp2 = p2.next
            p1.next = p2; p2.next = tmp1
            p1 = tmp1; p2 = tmp2
        return head1



if __name__ == '__main__':
	a = ListNode(0)
	b = ListNode(1)
	c = ListNode(2)
	d = ListNode(3)
	e = ListNode(4)
	f = ListNode(5)
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next=f
	res=Solution().reorderList(a)
	while res:
		print res.val
		res=res.next

	# aa = Solution().reorderList(a)
	# print aa.next.val


			






