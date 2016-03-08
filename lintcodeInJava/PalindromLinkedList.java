

/*Implement a function to check if a linked list is a palindrome.

Given 1->2->1, return true

Challenge: Could you do it in O(n) time and O(1) space?
*/

/*
分析：1  naive的做法，便利的同时存储元素，然后再在存储后的数组中判断 ＝》O(n)的空间复杂度
2: 我们是否能破坏原来链表的结构？一定要问面试官！
3: 由于事单链表，我们只能先便利一遍得到长度或者链表中间节点，才能继续操作，然后翻转中间节点后面的元素
4: 如果面试官说不能破坏原数据结构的话，我们需要人为恢复，即再次翻转中点后的元素
*/

//参考别人的代码 - O(n) time and space complexity

// This code would destroy the original structure of the linked list.
// If you do not want to destroy the structure, you can reserve the second part back.
public class Solution {
    /**
     * @param head a ListNode
     * @return a boolean
     */
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        }
        
        ListNode middle = findMiddle(head);
        middle.next = reverse(middle.next);
        
        ListNode p1 = head, p2 = middle.next;
        while (p1 != null && p2 != null && p1.val == p2.val) {
            p1 = p1.next;
            p2 = p2.next;
        }
        
        return p2 == null;
    }
    
    private ListNode findMiddle(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        return slow;
    }
    
    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        
        while (head != null) {
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        
        return prev;
    }
}