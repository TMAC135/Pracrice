

/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */ 
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: The new head of reversed linked list.
     */
     
    public ListNode reverse(ListNode head) 
    {
        if(head == null) return null;
        
        
        ListNode prev = head;
        ListNode cur = head.next;
        head.next = null;//now the head element is the tail element
        ListNode next;
        
        while(cur != null)
        {
            next = cur.next;
            cur.next = prev;
            
            // prepare for the next element
            prev = cur;
            cur = next;
        }
        return prev;
    }
}