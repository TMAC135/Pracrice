# Given a string s, partition s such that every substring of the
# partition is a palindrome. Return all possible palindrome partitioning of s

# example:
# s='aab', return [['aa','b'],['a','a','b']]
# s="abbab" return [["abba","b"],["a","b","bab"],["a","bb","a","b"],["a","b","b","a","b"]]

class Solution:
# My first naive solution, which I didn't enumerate all the 
# cases.
    # @param s, a string
    # @return a list of lists of string
    # def partition(self, s):
    #     # write your code here
    #     if not s:
    #     	return []
    #     res=[list(s)]
    #     for i in range(1,len(s)):
    #     	if self.valid(s[:i]) and self.valid(s[i:]):
    #     		res.append([s[:i],s[i:]])

    #     return res

    # def valid(self,string):
    # 	return string == string[::-1]
    """
    this is really a good dfs problem, several things need to be noticed:
    1: the input of the dfs function, in this problem, we need to list 
    	all the palindrome list, thus input should contain a string list
    2: the final result should store all the possible string lists, then a 
    	class attribute is a good choice - Solution.res
    3: when we meet the case where none list can't append, we can try concatenate
    	two lists which is essential equavalent to append operation. like 
    self.dfs(string[i:],stringlist+[string[:i]])

	reference: http://www.cnblogs.com/zuoyuan/p/3758437.html	
    """
    def partition(self,s):
    	Solution.res=[]
    	self.dfs(s,[])
    	return Solution.res

    def dfs(self,string,stringlist):
    	if string=='': Solution.res.append(stringlist)
    	for i in xrange(1,len(string)+1):
    		if self.valid(string[:i]):
    			self.dfs(string[i:],stringlist+[string[:i]])
    def valid(self,string):
    	return string == string[::-1]



if __name__=='__main__':
	test=['aab','a','ab','abaaba','acsews']
	for i in test:
		print Solution().partition(i)