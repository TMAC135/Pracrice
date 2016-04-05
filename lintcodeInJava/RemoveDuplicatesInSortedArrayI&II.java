/*从排好序的链表中删除重复元素，例如1->1->1->2->2->3
题目1: 仅保留一个重复节点 1->2->3
题目2: 删除全部的重复节点 3
*/

/*
注意：
基本思路都是对resHead 和 resTail 的操作，其中这两个节点是我们最后结果的头和尾部节点，但是
对resTail的每次操作后不要忘了将resTail.next设置为null,防止和原来的链表混幺。
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates1(ListNode head) 
    {
        if(head == null || head.next == null) return head;
        
        ListNode resHead = head;
        ListNode resTail = head;
        
        head = head.next;
        while(head != null)
        {
            // head = head.next;
            //also valid for the first iteration
            while(head != null && head.val == resTail.val)
            {
                head = head.next;
            }
            resTail.next = head;
            resTail = resTail.next;
            
            //judge whether the head is the end of the list
            if(head == null)
            {
                break;
            }else
            {
                head = head.next;
            }
        }

        return resHead;
        
    }
}

//////////////////////////////////////////////////////
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates2(ListNode head) 
    {
        if(head == null || head.next == null) return head;
        
        ListNode resHead = null;
        ListNode resTail = null;
        
        while(head != null)
        {
            ListNode tmp = head;
            head = head.next;
            while(head != null && head.val == tmp.val)
            {
                head = head.next;
            }
            if(tmp.next == head)
            {
                if(resTail == null)
                {
                    resHead = resTail = tmp;
                }else
                {
                    resTail.next = tmp;
                    resTail = resTail.next;
                }
                resTail.next = null;//very important, or the result will be messed with original list
            }
            
        }
        return resHead;
        
    }
}