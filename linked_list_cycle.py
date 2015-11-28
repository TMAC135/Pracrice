# coding=utf-8

"""
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true

Challenge
Follow up:
Can you solve it without using extra space?


"""



"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# without using any extra space
class Solution:
    # @param head, a ListNode
    # @return a boolean
    """
    解题思路：快慢指针技巧，slow指针和fast指针开始同时指向头结点head，fast每次走两步，slow每次走一步。
    如果链表不存在环，那么fast或者fast.next会先到None。如果链表中存在环路，则由于fast指针
    移动的速度是slow指针移动速度的两倍，所以在进入环路以后，两个指针迟早会相遇，如果在某一时刻slow==fast，说明链表存在环路.

    """

    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        