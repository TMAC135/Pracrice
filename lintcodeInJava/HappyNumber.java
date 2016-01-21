//coding=utf-8;
/** 
*Write an algorithm to determine if a number is happy.
*A happy number is a number defined by the following process: 
*Starting with any positive integer, replace the number by the sum of 
*the squares of its digits, and repeat the process until the number equals
* 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
*Those numbers for which this process ends in 1 are happy numbers
*
*/

/*
19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
*/

import java.util.*;

public class HappyNumber {
    /**
     * @param n an integer
     * @return true if this is a happy number or false
     */
    public boolean isHappy(int n) {
        // Write your code here
        if(n == 1) return true;
    	Set<Integer> mySet = new HashSet<Integer>();
    	mySet.add(n);
    	int tmp = n;
    	while(true){
    		tmp = compute(tmp);
// System.out.println(tmp);
    		//the case where we have periodic case
    		if(mySet.add(tmp) == false)  //method add when adding a non existing object,return true
    		{
    			return false;
    		}
    		//the case where we end up with getting 1
    		if(tmp == 1)
    		{
    			return true;
    		}
    	}

    }

    /*Compute the number after bit square manipulation
    */
    public static int compute(int n){
    	int sum = 0;
    	int mod = 0;
    	while(n/10 != 0){
    		mod = n%10;
// System.out.println("  "+mod);
    		sum += Math.pow(mod,2);
// System.out.println("   "+ sum;   		
    		n = n/10; 
    	}
    	sum += Math.pow(n,2);
    	return sum;
    }

    //the test code
    public static void main(String[] args) {
    	HappyNumber myHappyNumber = new HappyNumber();
    	int[] mytest = new int[]{19};
    	for(int i:mytest){
    	System.out.println(myHappyNumber.isHappy(i));
    }
    }
}