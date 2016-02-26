
/*
Given a digit string, return all possible letter combinations that the number could represent.

Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
*/



//我的第一次解法，BFS,每次都new出新对象
public class Solution {
    /**
     * @param digits A digital string
     * @return all posible letter combinations
     */
    public ArrayList<String> letterCombinations(String digits) 
    {
        //set up the dictionary for the letter->digit
        HashMap<Character,String> dict = new HashMap<>();
        dict.put('2',"abc");
        dict.put('3',"def");
        dict.put('4',"ghi");
        dict.put('5',"jkl");
        dict.put('6',"mno");
        dict.put('7',"pqrs");
        dict.put('8',"tuv");
        dict.put('9',"wxyz");
      
        ArrayList<String> res = new ArrayList<>();
        if(digits == null || digits.length() == 0) return res;
      
        for(int i=0;i<digits.length();i++)
        {
          if(res != null) 
          {
            //the case the input is not digit,we ignore it
            if(digits.charAt(i) - '0' < 0 || digits.charAt(i) - '0'>9) continue;
            String tmp = dict.get(digits.charAt(i));
            ArrayList<String> cur = new ArrayList<>();
            for(String iter:res)
            {
              for(char add:tmp.toCharArray())
              {
                cur.add(iter + add);
              }
            }
            res = cur;
          }else
          {
            if(digits.charAt(i) - '0' < 0 || digits.charAt(i) - '0' > 9) continue;
            String tmp = dict.get(digits.charAt(i));
            for(char add:tmp.toCharArray())
            {
              res.add("" + add);
            }
          }
        }
      return res;
    }
}


//dfs解法： 效率闭bfs要低，因为重复操作元素了
public class Solution {
    /**
     * @param digits A digital string
     * @return all posible letter combinations
     */

    private HashMap<Character,String> dict;

    private void setUp()
    {
    	dict.put('2',"abc");
        dict.put('3',"def");
        dict.put('4',"ghi");
        dict.put('5',"jkl");
        dict.put('6',"mno");
        dict.put('7',"pqrs");
        dict.put('8',"tuv");
        dict.put('9',"wxyz");

    }

    public ArrayList<String> letterCombinations(String digits) 
    {	
        HashMap<Character,String> dict = new HashMap<Character,String>();
    	dict.put('2',"abc");
        dict.put('3',"def");
        dict.put('4',"ghi");
        dict.put('5',"jkl");
        dict.put('6',"mno");
        dict.put('7',"pqrs");
        dict.put('8',"tuv");
        dict.put('9',"wxyz");
      
        ArrayList<String> res = new ArrayList<>();
        if(digits == null || digits.length() == 0) return res;
        dfs(res,digits,0,"",dict);
        return res;
      
    }

    public void dfs(ArrayList<String> res,String digits,int index,String tmp,HashMap<Character,String> dict)
    {
    	//edge case
    	if(index >= digits.length())
    	{
    	    res.add(tmp);
    	    return;//不要忘了return
    	}

    	if(digits.charAt(index) - '0' < 0 || digits.charAt(index) - '0' > 9) dfs(res,digits,index+1,tmp,dict);
    	else
    	{
    		String value = dict.get(digits.charAt(index));
    		for(char add:value.toCharArray())
    		{
    			dfs(res,digits,index+1,tmp+add,dict);
    		}
    	}
    }

}
