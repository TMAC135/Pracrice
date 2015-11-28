# coding=utf-8

"""
Based on I:题意：如果链表中存在环路，找到环路的起点节点。

思路：在fast指针和slow指针相遇后，fast指针不动，slow指针回到head，
然后slow指针和fast指针同时向前走，只不过这一次两个指针都是一步一步向前走。两个指针相遇的节点就是环路的起点。

证明：http://www.cnblogs.com/zuoyuan/p/3701877.html

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None