


// Write a function that will convert an integer into it's English language equivalent.
//
// Ex:
//
// 56 => 'fifty six'
// 1024 => 'one thousand twenty four'
// 65536 => 'sixty five thousand five hundred thirty six'
// 500500 => 'five hundred thousand five hundred'
//
// Notes:
// a) Assume a non-null, non-negative value with a maximum bound of 1,000,000,000 (0 <= n <= 1,000,000,000).
// b) No need to include 'and', commas, periods, etc.



public class Solution
{
  
  
  public static void convert(int num)
  {
    if(nums == 0) return "Zero";
    
    int flag = 0;
    String res = "";
    int digit=0;
    HashMap<Integer,String> dict = new HashMap<Integer,String>();
    //put all key-value to the dictionary
    
    
    while(nums % 10 != 0)
    {
      digit++;
      int temp = nums % 10;
      
      //case for different case ,hundred, thousand,million,billion
      if(digits == 4)
      {
        res += dict.get(temp) + "thousand";
      }else if(digits == 7)
      {
        res += dict.get(temp) + "million";
      }else if(digits == 10)
      {
          res += dict.get(temp) + "billion";
      }

    }
    
    
  }
  
}