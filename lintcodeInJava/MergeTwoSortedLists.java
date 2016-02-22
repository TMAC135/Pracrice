

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

//merge two sorted lists
public class Solution 
{
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) 
    {
      //declare for the merged list
      ListNode dummy = new ListNode(0);
      ListNode cur = dummy;
      //two pointers for passing the two lists
      ListNode p1 = l1;
      ListNode p2 = l2;
      
      while(p1 != null && p2 != null)
      {
        if(p1.val <= p2.val)
        {
          cur.next = p1;
          p1 = p1.next;
        }else
        {
          cur.next = p2;
          p2 = p2.next;
        }
        cur = cur.next;
      }
      
      if(p1 == null)
      {
        cur.next = p2;
      }else
      {
        cur.next = p1;
      }
      return dummy.next;
    }
}