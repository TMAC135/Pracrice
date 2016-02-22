


/*

*/

public class Solution 
{
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
  /*
  what is the case if any one of these two strings are null or empty string
  */

  //我的解法，开始有几个bug,使用了stack 和 stringbuilder,但是memory limit exceed
    public String addBinary(String a, String b) 
    {
      Stack<Character> stack = new Stack<>();
      //null case
      if(a == null || a.length() == 0) return b;
      if(b == null || b.length() == 0) return a;
      
      boolean carry = false;
      for(int i=Math.max(a.length(),b.length())-1; i <= 0;i--)
          {
            // we can have a function to get the char at a certain index for a string
            //valid char for a
            char tmp1;
            char tmp2;
            if(i >= 0)
            {
              tmp1 = a.charAt(i);
            }else
            {
              tmp1 = '0';
            }
            //valid char for b
            if(i >= 0)
            {
              tmp2 = b.charAt(i);
            }else
            {
              tmp2 = '0';
            }
        
            //four cases for add 
            if(tmp1 == tmp2 && carry == true)
            {
              stack.push('1');
              if(tmp1 == '1') carry = true;
              else carry = false;
              
            }else if(tmp1 == tmp2 && carry == false)
            {
              stack.push('0');
              if(tmp1 == '1') carry = true;
              else carry = false;
            }else if (tmp1 != tmp2 && carry == true)
            {
              stack.push('0');
              carry = true;
            }else
            {
              stack.push('1');
              carry = false;
            }
          }
      //check for the last carry
      if(carry == true)
      {
        stack.push('1');
      }
      StringBuilder sb = new StringBuilder();
      //build the string given the stack
      for(int j=0;j<stack.size();j++)
      {
        sb.append(stack.pop()); 
      }
      return sb.toString();
      
    }


    //别人的解法，思路一样，但是更加巧妙
      public String addBinary(String a, String b) {
     int m = a.length();
     int n = b.length();
     int carry = 0;
     String res = "";
     // the final length of the result depends on the bigger length between a and b, 
     // (also the value of carry, if carry = 1, add "1" at the head of result, otherwise)
     int maxLen = Math.max(m, n);
     for (int i = 0; i < maxLen; i++) {
         // start from last char of a and b
         // notice that left side is int and right side is char
         // so we need to  minus the decimal value of '0'
         int p=0,q=0;
         if(i<m)
             p = a.charAt(m-1-i) - '0';
         else
             p = 0;
         
         if(i<n)
             q = b.charAt(n-1-i)-'0';
         else
             q = 0;
             
         int tmp = p + q + carry;
         carry = tmp / 2;
         res += tmp % 2;
     }
     return (carry == 0) ? res : "1" + res;
     }
}