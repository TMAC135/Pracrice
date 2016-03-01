



/*
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
*/



//第一次解法，没有考虑数字可以结合的，如例子："105", 5 -> ["1*0+5","10-5"]，以后看题一定要认真！！！！！！
/* Brain storm
solve the problem recursively
for every string, we divide it as two part, one the first digit, the second part is 
the substring which is exclude the first digit. 
*/

/*clarifications
1: how is the case where the string contain the non-digit char?
2: do we need to consider to consider the case of overflow?
*/
public class Solution 
{
    public List<String> addOperators(String num, int target) 
    {
      List<String> res = new ArrayList<String>();
      
      //special cases
      if(num == null || num.length() == 0) res;
       
      ArrayList<String> tmp = new ArrayList<>();
      helper(target,num,res,tmp,0);
      return res;
    }
  
  
    //pay attention to the case where the * operator, we need a prev to 
    //store the previous result
    public void helper(int target,String num,List<String> res,ArrayList<String> tmp,int prev)
    {
      //edge case
      if(num == null) return;
      if(num.length == 1)
      {
        if(Integer.parseInt(num) == target || prev*Integer.parseInt(num) == target) res.append(tmp+num);
        else return;
      }
      
      
      //extract the first digit,need to consider the case which non-digit char
      char digitChar = num.charAt(0);
      int digit = digitChar - '0';

      
      
      // little bit redundant
      if(prev == 0){
      //+
      String nextAdd = tmp + digitChar + "+";
      helper(target - digit,num.subString(1),res,nextAdd,0);
      //-
      String nextMinus = tmp + digitChar + "-";
      helper(digit - targer,num.subString(1),res,nextMinus,0);
      
      //*, little different from above, if we must bound with the next digit
      String nextMul = tmp + digitChar + "*";
      helper(target,num.subString(1),res,nextMul,digit);
      }else
      {
      String nextAdd = tmp + digitChar + "+";
      helper(target - prev*digit,num.subString(1),res,nextAdd,0);
      //-
      String nextMinus = tmp + digitChar + "-";
      helper(digit*prev - target,num.subString(1),res,nextMinus,0);
      
      //*, little different from above, if we must bound with the next digit
      String nextMul = tmp + digitChar + "*";
      helper(target,num.subString(1),res,nextMul,prev*digit);
        
      }     

    }
}


//别人的解法，也是通过dfs来做的，不过递归需要维持两个参数，这题的难点就是如何正确找到cur 和 diff
//cur代表截止到该index时候，我们得到的值是多少，diff代表的是上一个数字是多少，维护这个数字的原因是为了
//处理乘法的因子，例如：
/*
for example, if current value is 3, last diff is 2 next vaue is 4
+ for next loop, current value is 3 +4, diff is 4
- for next loop, current value is 3-4, diff is -3

* for next loop, current value is (3-2) + 2 *4, diff is 2*4
*/

public List<String> addOperators(String num, int target) {  
        List<String> res = new ArrayList<String>();  
        dfs(num, target, 0, 0, "", res);  
        return res;  
    }  
    public void dfs(String num, int target, long cur, long diff, String temp, List<String> res) {  
        if(cur == target && num.length() == 0) {  
            res.add(temp);  
        }  

        //由于数字不一定是单个的，我们需要枚举所有数字的可能，因此复杂度很高
        for(int i = 1; i<=num.length(); i++) {  
            String str = num.substring(0, i);  
            if(str.length()>1 && '0' == str.charAt(0)) return; //特殊的情况：全部都是0
            String next = num.substring(i);  
            if(temp.length() >0) {  
                dfs(next, target, Long.parseLong(str) + cur, Long.parseLong(str), temp + "+" +str, res);  
                dfs(next, target, cur - Long.parseLong(str), -Long.parseLong(str), temp + "-" +str, res);  
                dfs(next, target, (cur - diff) + diff * Long.parseLong(str), Long.parseLong(str)*diff, temp + "*" +str, res);  
            } else {  
                dfs(next, target, Long.parseLong(str), Long.parseLong(str), str, res);  
            }  
        }  
    }






