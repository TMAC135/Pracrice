
/*
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the"
*/

/*
What constitutes a word?
A sequence of non-space characters constitutes a word.

Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.

How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
*/

public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */

     //没有用jdk的库文件，通过一个指针从后向前移动来判断什么时候找到一个单词，
    public String reverseWords(String s) 
    {

    	if(s == null || s.length() == 0) return "";
    	StringBuffer sb = new StringBuffer();

    	int i = s.length()-1;
    	int end = 0;
    	int start = 0;
    	boolean word = false;
    	while(i >= 0)
    	{
    		if(s.charAt(i) != ' ')
    		{
    			if(!word) 
    			{
    				end = i;
    				word = true;
    			}
    		}else
    		{
    			if(word) 
    			{
    				start = i+1;
    				sb.append(s.substring(start,end+1));
    				sb.append(' ');
    				word = false;
    			}
    		}
    		i--;
    	}
    	//the case where there are no space in the begining of the string
    	if (s.charAt(0) != ' ') sb.append(s.substring(0,end+1));
    	return sb.toString().trim();
    }

}


//通过s.split(' ')来生成一个数组再调用Collections.reverse()生成倒叙的数组

public static String reverseWords(String s) {
         if(s==null||s.length()==0)
             return s;
         String [] result = s.split(" ");
         if(result==null||result.length==0)
             return "";
        //注意，"33   34"中间右多个空格时候，我们在分单词的时候也会产生很多空格，我们需要判断并移除   
         ArrayList<String> list = new ArrayList<String>();
         
         for(int i = 0; i<result.length;i++){
             if(!result[i].isEmpty())
                 list.add(result[i]);
         }
         Collections.reverse(list);
         
         String ans = new String();
         for(int i = 0; i<list.size()-1;i++){
             ans += list.get(i)+" ";
         }
         ans +=list.get(list.size()-1);
         return ans;
     }