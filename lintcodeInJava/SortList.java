/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode sortList(ListNode head) 
    {
        if(head == null) return null;
        if(head.next == null) return head;//this base case is very import or it will produce infinite loop
        
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode sortList2 = sortList(slow.next);
        slow.next = null;//we need to cut the list in the between
        ListNode sortList1 = sortList(head);
        //merge two sorted list
        ListNode res = new ListNode(0);
        ListNode dummy = res;
        while(sortList1 != null && sortList2 != null){
            if(sortList1.val <= sortList2.val){
                res.next = sortList1;
                sortList1 = sortList1.next;
            }else{
                res.next = sortList2;
                sortList2 = sortList2.next;
            }
            res = res.next;
        }
        
        if(sortList1 == null){
            res.next = sortList2;
        }else{
            res.next = sortList1;
        }
        return dummy.next;
    }
}