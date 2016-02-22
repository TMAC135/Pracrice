
/**
*Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
*/

/*
拓展题：找到一个字符串的最大子回文字符串，或者找到所有的回文字符串
两题的思路应该一样，依次遍历每个字符，然后以该字符为中心，向两边扩展然后找到
最大的回文字符串，注意扩展的时候有两中情况（奇偶），以一个字符为中心，以两个字符为中心。
*/

public class Solution 
{
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
	public boolean isPalindrome(String s) 
	    {
	    	// bound case
	    	if (s == null || s.length() == 0)
	    	{
	    		return true;
	    	}
	    	int first = 0;
	    	int last = s.length() -1;

	    	while(first < last)
	    	{
	    		// judge if the char is space or not
	    		if ( !helper(s.charAt(first)) ) first++;
	    		else if ( !helper(s.charAt(last)) ) last--;
	    		else
	    		{
	    		    int gap = Math.abs(s.charAt(first) - s.charAt(last));
	    			if (gap == 0 || gap == 'a' - 'A' ) 
	    			{
	        			first++;
	        			last--;
	    			}else
	    			{
	    			    return false;
	    			}
	    		}
	    	}
	    	return true;
	    }

    static char char_0 = '0';
    static char char_9 = '9';
    static char char_a = 'a';
    static char char_z = 'z';
    static char char_A = 'A';
    static char char_Z = 'Z';
    final static int NUMBER_0 = (int)char_0;
    final static int NUMBER_9 = (int)char_9;
    final static int ALPHA__LOWER_A = (int)char_a;
    final static int ALPHA__LOWER_Z = (int)char_z;
    final static int ALPHA__UPPER_A = (int)char_A;
    final static int ALPHA__UPPER_Z = (int)char_Z;

    //helper function to determine whether the char is alphanumeric
    public static boolean helper(char _c)
    {
    	int tmp = (int)_c;
    	return ((tmp >= NUMBER_0 && tmp <=NUMBER_9) || (tmp >= ALPHA__LOWER_A && tmp <= ALPHA__LOWER_Z) || 
    			(tmp >= ALPHA__UPPER_A && tmp <= ALPHA__UPPER_Z));
    }
}


// notice that we can convert the lower case to upper case, 
// for chars, we can judge the relations
class Solution2
{
	  public static boolean isPalindrome(String s) {
              if(s.length()==0)
                 return true;
              
              s = s.toUpperCase();
              int low1 = 'A', high1 = 'Z';
              int low2 = '0', high2 = '9';
              int low = 0, high = s.length()-1;
              
             while(low < high){
                 if((s.charAt(low)<low1||s.charAt(low)>high1)
                     && (s.charAt(low)<low2||s.charAt(low)>high2)){
                         low++;
                         continue;
                     }
                     
                 if((s.charAt(high)<low1||s.charAt(high)>high1)
                     && (s.charAt(high)<low2||s.charAt(high)>high2)){
                         high--;
                         continue;
                     }
                 if(s.charAt(low) == s.charAt(high)){
                     low++;
                     high--;
                 }else
                     return false;
             }
             return true;
         }
}