

/*
递归的思想
*/
import java.util.*;


/*
题目描述

对于三个字符串A，B，C。我们称C由A和B交错组成当且仅当C包含且仅包含A，B中所有字符，且对应的顺序不改变。请编写一个高效算法，判断C串是否由A和B交错组成。
给定三个字符串A,B和C，及他们的长度。请返回一个bool值，代表C是否由A和B交错组成。保证三个串的长度均小于等于100。
测试样例：
"ABC",3,"12C",3,"A12BCC",6
返回：true
*/
public class Mixture {
    public boolean chkMixture(String A, int n, String B, int m, String C, int v) {
        // write code here
        if(n == 0 && m == 0) return true;
        if(v != (n+m)) return false;
        
        
        /*  有问题，当判断的元素和两个都相等时，这种方法可能不对，因此需要对两种情况都判断
        for(int i=0;i<v;i++){
            if(C.charAt(i) == A.charAt(index1)) index1++;
            else if(C.charAt(i) == B.charAt(index2)) index2++;
            else return false;
        }
        return true;
        */
        return helper(A,0,B,0,C,0);
    }
    
    
    
    public boolean helper(String A,int index1,String B,int index2,String C, int cur){
        //edge case
        
        if(cur == C.length()) return true;
        
        if(index1 == A.length()){
            if(B.charAt(index2) == C.charAt(cur)) return helper(A,index1,B,index2+1,C,cur+1);
            else return false;
        }
        
        if(index2 == B.length()){
            if(A.charAt(index1) == C.charAt(cur)) return helper(A,index1+1,B,index2,C,cur+1);
            else return false;
        }
        
        
        if(C.charAt(cur) != A.charAt(index1) && C.charAt(cur) != B.charAt(index2)) 
            return false;
            
        boolean nextA = helper(A,index1+1,B,index2,C,cur+1);
        boolean nextB = helper(A,index1,B,index2+1,C,cur+1);
        if(C.charAt(cur) == A.charAt(index1) && C.charAt(cur) == B.charAt(index2))
            return nextA || nextB;
        else if(C.charAt(cur) == A.charAt(index1)) return nextA;
        else return nextB;

    }
}


//别人的答案，同样使用递归，感觉更巧妙一点，是从后往前匹配,这样在判断edge case 的时候就容易判断了
public static boolean chkMixture(String A,String B, String C,int i,int j,int k){
    	//edge case
        if(k == 0){
            return true;
        }
        if(i == 0){
            if(B.charAt(j) == C.charAt(k)){
                return chkMixture(A,B,C,0,j-1,k-1);
            }else{
                return false;
            }
        }
        if(j == 0){
            if(A.charAt(i) == C.charAt(k)){
                return chkMixture(A,B,C,i-1,0,k-1);
            }else{
                return false;
            }
        }
    
    	
        boolean res1 = false;
        boolean res2 = false;
        if(A.charAt(i) == C.charAt(k)){
            res1 = chkMixture(A,B,C,i-1,j,k-1);
        }
        if(B.charAt(j) == C.charAt(k)){
            res2 = chkMixture(A,B,C,i,j-1,k-1);
        }
        return res1||res2;
    }

