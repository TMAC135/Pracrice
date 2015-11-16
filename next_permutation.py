# coding=utf-8

"""
Given a list of integers, which denote a permutation.
Find the next permutation in ascending order.

Example
For [1,3,2,3], the next permutation is [1,3,3,2]
For [4,3,2,1], the next permutation is [1,2,3,4]

Note
The list may contains duplicate integers.

"""

class Solution:
    # @param num :  a list of integer
    # @return : a list of integer

    """
    the method here we use is based on the permutation in recursion way, but 
    # memory limit exceed!!!!
    """
    def nextPermutation1(self, num):
        # write your code here
        if not num:
        	return None
        list_all=num[:]
        list_all.sort()
        res=[]
        self.recursion(list_all,[],res)
        # return res
        return res[res.index(num)+1] if res.index(num)<len(res)-1 else res[0]


    def recursion1(self,array,tmp,res):
    	if not array:
    		res.append(tmp)
    	prev = None
    	for i in xrange(len(array)):
    		if array[i] != prev:
    			self.recursion(array[:i]+array[(i+1):],tmp+[array[i]],res)
    		prev=array[i]

    """
    modify the method above, we don't actually store all the permutations in res, instead we 
    determine the location of num and return the next permutation.

    this method is time limit exceed!!!!!

    """
    def nextPermutation2(self, num):
        # write your code here
        if not num:
        	return None
        list_all=num[:]
        list_all.sort()
        indicator=[0]
        res=[]
        self.recursion(list_all,[],num,res,indicator)
        return res[0] if res else list_all
        

    def recursion2(self,array,tmp,num,res,indicator):
    	if not array:
    		# res.append(tmp)
    		if indicator[0] == 1:
    			res.append(tmp)
    			indicator[0]= 0
    		if tmp == num:
    			indicator[0] = 1
    	prev = None
    	for i in xrange(len(array)):
    		if array[i] != prev:
    			self.recursion(array[:i]+array[(i+1):],tmp+[array[i]],num,res,indicator)
    		prev=array[i]


    """
    in this method, we will walk the array in the reverse direction

    此题类似与给定一个数值，求出下一个大于此值的数值，且此数值只能有原来的数字组成。
    """
    def nextPermutation3(self, num):
        # write your code here
        if not num:
        	return None
        List=[]
        prev=-999999
        for i in xrange(len(num)-1,-1,-1):
        	if num[i] >= prev:
        		List.append(num[i])
        		prev=num[i]
        	else:
        		next=self.insertion(num[i],List)
        		List=[next] + List
        		break

        return num[:i] + List 

    # we insert the number into the list but the same time we return the next value
    # use binary method
    def insertion(self,num,List):
    	s=0
    	e=len(List)-1

    	# while的条件限制了最后s 与 e 相差一位。
    	while s < e-1:
    		m = (s+e)/2
    		if List[m] > num:
    			e = m
    		else:
    			s=m
    	# 注意边界检查，当我们用binary search 时，特别注意这点。
    	# 此题我们只确定开始的 List[e] > num, 但并不能确定最开始的 List[s] 与 num 的关系
    	# 因此需要在最后退出while后另行检查。
    	if List[s] > num:
    		tmp=List[s]
    		List[s] = num
    	else:
	    	tmp = List[e]
	    	List[e] = num
    	return tmp



if __name__ == '__main__':
	print Solution().insertion(1,[2,3])
	print Solution().nextPermutation3([1,3,2])


