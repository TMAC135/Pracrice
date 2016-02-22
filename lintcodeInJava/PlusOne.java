

/*
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
*/


//注意细节问题，不要数组越界，定义数组不要忘了[]，^~^
public class Solution {
    /**
     * @param digits a number represented as an array of digits
     * @return the result
     */
    public int[] plusOne(int[] digits) 
    {
      //what's the case where the array is an empty array, should i return 1 or just an empty array?
      if(digits == null) return null;
      if(digits.length == 0) return digits;
      
      int index = digits.length-1;
      while(index >= 0)
      {
        if(digits[index] != 9)
        {
          digits[index]++;
          return digits;
        }else
        {
          digits[index--]=0;
        }
      }
      //otherwise we come across the case of overflow
      int[] res = new int[digits.length+1];
      res[0]=1;
      return res;
    }
  
}