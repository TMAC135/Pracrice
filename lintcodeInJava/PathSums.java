

import java.util.*;

/*
 题目描述

现在有一个城市销售经理，需要从公司出发，去拜访市内的商家，已知他的位置以及商家的位置，但是由于城市道路交通的原因，他只能在左右中选择一个方向，在上下中选择一个方向，现在问他有多少种方案到达商家地址。
给定一个地图map及它的长宽n和m，其中1代表经理位置，2代表商家位置，-1代表不能经过的地区，0代表可以经过的地区，请返回方案数，保证一定存在合法路径。保证矩阵的长宽都小于等于10。
测试样例：
[[0,1,0],[2,0,0]],2,3
返回：2 
 */

/*这题的描述有问题：：：：
此题有点复杂，首先得找到起始点和结束点，然后根据两个点决定x,y对应得步长大小，
最后使用动态规划得思想对两点构成得区域进行计算。
注意：此题可以直接在原数组操作，如果不可以，我们需要另外开辟空间进行计数
*/

/*
此题有点复杂，首先得找到起始点和结束点，然后根据两个点决定x,y对应得步长大小，
最后使用动态规划得思想对两点构成得区域进行计算。
注意：此题可以直接在原数组操作，如果不可以，我们需要另外开辟空间进行计数
*/

public class Visit {
    public int countPath(int[][] map, int n, int m) {
        // write code here
        
        //find start and end point firstly
        int startX=-1;
        int startY=-1;
        int endX=-1;
        int endY=-1;
        for(int i = 0; i < n; i++){
            
            for(int j = 0; j< m ; j++){
                if(map[i][j] == 1){
                    startX = i;
                    startY = j;
                    if(endY != -1) break;
                }
                if(map[i][j] == 2){
                    endX = i;
                    endY = j;
                    if(startX != -1) break;
                }
            }
        }
        
        //determine the step size for both x and y direction based on the start ans end points
        int stepX = (startX > endX)?-1:1;
        int stepY = (startY > endY)?-1:1;
        
//        return stepX;
//        
//        //initilize the margin element of the region
        boolean flag = false;
        for(int i=startX; i != endX + stepX; i+=stepX){
        	if(flag == false){
        		if(map[i][startY] == -1){
        			map[i][startY] = 0;
        			flag = true;
        		}else map[i][startY] =1;
        	}else map[i][startY]= 0;
        	
            //map[i][startY]=(map[i][startY] == -1)?0:map[i-stepX][startY];
        }
        flag=false;
        for(int j=startY; j!=endY+stepY; j+=stepY){
        	if(flag == false){
        		if(map[startX][j] == -1){
        			map[startX][j] = 0;
        			flag = true;
        		}else map[startX][j] = 1;
        	}else map[startX][j]= 0;        	
            //map[startX][j]=(map[startX][j] == -1)?0:map[startX][j-stepY];
        }
//        return map;
        
        for(int i=startX+stepX;i != endX+stepX; i+=stepX){
            
            for(int j=startY+stepY;j != endY+stepY;j+=stepY){
                map[i][j]=(map[i][j] == -1)?0:map[i-stepX][j]+map[i][j-stepY];
            }
        }
        return map[endX][endY];
    }
}
