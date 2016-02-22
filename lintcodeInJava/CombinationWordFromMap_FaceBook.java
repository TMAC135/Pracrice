
/*

2.19日下午三点Facebook一面跪经总结
可怜兮兮地只做了一道题：. 1point 3acres 璁哄潧
input: a string (eg. "cat"). 鐗涗汉浜戦泦,涓€浜╀笁鍒嗗湴
input: a map (eg. c -> [c, C, %], a -> [a, A, *], t -> [t, T, &])
output all the combination: cat, Cat, %at, .....
*/


import java.util.*;

public class Solution
{
	public static void main(String[] args) 
	{
		String input = "abc";
		Map<Character,char[]> stringMap =new HashMap<Character, char[]>();
		char[] aa ={'a','A','%'};
		stringMap.put('a', aa);
		char[] bb ={'b','B','$'};
		stringMap.put('b', bb);
		char[] cc ={'c','C','%'};
		stringMap.put('c', cc);
		
		Solution solution = new Solution();
		HashSet<String> res = new HashSet<String>();
		res = solution.combination(input, stringMap);
//		res.add("aa");
//		res.add("bb");
		System.out.println(res);
		System.out.println(res.size());
				
	}
  
  /*
  1: do we guarantee that the value of map contain the key itself?
  if so, cat: c->[c,C,%] a->[a,A,&] t->[t,T,*]
          1: cat,Cat,%at
  2:do we need to consider the duplicated case?       
  */
	
	//第一种方法，利用递归来求解，但是不知道为什么有异常,
  	//递归也可以是有返回值的版本
  public HashSet<String> combination(String input, Map<Character,char[]> stringMap)
  {
    HashSet<String> res = new HashSet<String>();
    if(input == null || input.length() == 0) return res;
    
    StringBuilder sb = new StringBuilder();
    helper(input,res,0,sb,stringMap);
    return res;
  }
  
  public void helper(String str,HashSet<String> res,int index,StringBuilder sb,Map<Character,char[]> stringMap)
  {
      for(char cur:stringMap.get(str.charAt(index)))
      {
        StringBuilder sbNext = new StringBuilder(sb);
        sbNext.append(cur);
        if(index < str.length()-1)
        {
          helper(str,res,index+1,sbNext,stringMap);
        }else res.add(sbNext.toString());
      }

  }
  
  //第二种放法，类似于permutation的做法，遍历string,每次往里面一个元素的所有情况
  public HashSet<String> combination2(String input, Map<Character,char[]> stringMap)
  {
    HashSet<String> res = new HashSet<String>();
    res.add("");
    if(input == null || input.length() == 0) return res;
    
    for(int i=0;i<input.length();i++)
    {
    	HashSet<String> next = new HashSet<String>();
    	char[] map = stringMap.get(input.charAt(i));
    	
    	for(String str:res)
    	{
//    		StringBuilder sb = new StringBuilder(str);
    		for(int j=0;j<map.length;j++)
    		{
    			next.add(str + map[j]);
    		}
    	}
    	res = next;
    	
    }
    return res;
  }
  
  
}