
/*
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.
*/

/*
Example
Given n = 5, return "111221".
*/



//我的解法，调了几个bug,最终成功
public class Solution {
    /**
     * @param n the nth
     * @return the nth sequence
     */
    public String countAndSay(int n) 
    {
      if(n <= 0) return null;
      
      StringBuilder sb = new StringBuilder();
      sb.append('1');
      
      char prev = '1';
      char cur;
      int count = 1;
        
      for(int i=0; i<n-1; i++)
      {
        StringBuilder tmp = new StringBuilder();
        prev = sb.charAt(0);
        count = 1;
        for(int j=1;j<sb.length();j++)
        {
          cur = sb.charAt(j);
          if(prev == cur) count++;
          else 
          {
              tmp.append(Integer.toString(count)).append(prev);
              prev = cur;
              count = 1;
          }
        }
        sb = tmp;
        sb.append(Integer.toString(count)).append(prev);
      }
      return sb.toString();
    }
}