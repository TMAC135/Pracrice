#coding=utf-8
"""
Ugly number is a number that only have factors 3, 5 and 7.
Design an algorithm to find the Kth ugly number. The first 5 ugly numbers are 3, 5, 7, 9, 15 ...

Example
If K=4, return 9

Challenge
O(K log K) or O(K) time

"""

class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.

    main reference: http://bookshadow.com/weblog/2015/08/19/leetcode-ugly-number-ii/

    Notice that all the ugly number must be the previous ugly number *3 or *5 or *7,
    using this fact, we will divide these numbers into 3 stacks and pop 1 element
    once a time from these 3 stacks, here is the example for the case 2,3,5,same 
    principle apply for the 3,5,7:

    丑陋数序列可以拆分为下面3个子列表：

	(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
	(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
	(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
	我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5

	接下来我们使用与归并排序相似的合并方法，从3个子列表中获取丑陋数。每一步我们从中选出最小的一个，然后向后移动一步。
    """
    def kthPrimeNumber(self, k):
        # write your code here
        if k<1:
        	return 0

        # first way I do, which is not the hint means
        # stack3,stack5,stack7=[3],[5],[7]
        # # res=[]
        # for _ in xrange(k):
        # 	min_pop=min(stack3[0],stack5[0],stack7[0])
        # 	if min_pop==stack3[0]:
        # 		stack3.pop(0)
        # 	elif min_pop==stack5[0]:
        # 		stack5.pop(0)
        # 	else:
        # 		stack7.pop(0)
        # 	stack3.append(min_pop*3)
        # 	stack5.append(min_pop*5)
        # 	stack7.append(min_pop*7)
        # 	# res.append(min_pop)

        n3,n5,n7=0,0,0
        res=[1]
        for _ in xrange(k):
        	m3,m5,m7=res[n3]*3,res[n5]*5,res[n7]*7
        	min_push=min(m3,m5,m7)
        	if min_push==m3:
        		n3+=1
        	if min_push==m5:
        		n5+=1
        	if min_push==m7:
        		n7+=1
        	res.append(min_push)
        return res[-1]


if __name__=='__main__':
	print Solution().kthPrimeNumber(19)



		





"""
another problem of ugly number:
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
Note that 1 is typically treated as an ugly number

this problem is much easier,here is one java solution:
我们不断整除2，3，5直到其不能被除尽，然后判断最后结果是否是1.
"""

"""
public boolean isUgly(int num) {
        
        if(num<=0) return false;  
        if(num==1) return true;  
          
        while(num>=2 && num%2==0) num/=2;  
        while(num>=3 && num%3==0) num/=3;  
        while(num>=5 && num%5==0) num/=5;  
          
        return num==1;  
    }

"""