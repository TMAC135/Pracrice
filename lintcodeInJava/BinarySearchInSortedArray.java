

import java.util.*;

/*
第一种方法：正常二分发，当找到元素时候，向左查找排除重复，这种方法最坏可能到O(n)的时间复杂度，不是最优解
第二种方法：二分的条件下保证left<val，right >= val,并且最后判断right 是否是给定的val
*/

public class BinarySearch {
    //方法1:正常二分发，当找到元素时候，向左查找排除重复，这种方法最坏可能到O(n)的时间复杂度，不是最优解
    public int getPos1(int[] A, int n, int val) {
        // write code here
        if(n <= 0) return -1;
        int left = 0;
        int right = n-1;
        int mid=0;
        boolean flag = false;
        while(left <= right){
            mid = (left + right)/2;
            if(A[mid] == val){
                flag = true;
                break;
            }else if(A[mid] > val){
                right = mid -1;
            }else{
                left = mid +1;
            }
            
        }
        if(flag == false) return -1;
        else{
            while(mid >= 0 && A[mid] == val){
				mid--;                
            }
            return mid+1;
        }
    }
    
    
    
    // 方法2:二分的条件下保证left<val，right >= val,并且最后判断right 是否是给定的val
    public int getPos2(int[] A, int n, int val) {
        // write code here
		if(n <= 0) return -1;
        if(A[0] > val || A[n-1] < val) return -1;
        if(A[0] == val) return 0;
        
        int left =0;
        int right = n-1;
        int mid = 0;
        while(left < right - 1){
            mid = (left+right)/2;
            if(A[mid] < val) left =mid;
            else right = mid;
        }
        return (A[right] == val)?right:-1;
    }    
}