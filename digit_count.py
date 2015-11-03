"""
Count the number of k's between 0 and n. k can be 0 - 9.

Example
if n=12, k=1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], we have FIVE 1's (1, 10, 11, 12)

"""

class Solution:
		# @param k & n  two integer
		# @return ans a integer
		"""
		Brute force method, we simply walk through all numbers and 
		add the count.
		of course this method is time consuming.
		"""
		def digitCounts(self, k, n):
			res=0
			if k==0:
				return (n/10)+1
			else:
				for i in xrange(1,n+1):
					res += self.Count(i,k)
				return res

		def Count(self,i,k):
			res=0
			while i:
				res+=((i%10)==k)
				i=i/10
			return res
		"""
		This method is based on the analysis for the different digits.
		we build the relationship between the current digit and higher digit.
		It is not that easy to find this relationship.

		for more explicit reference, see 
		http://www.cnblogs.com/EdwardLiu/p/4274497.html

		Notice that since we add the digit count, so we can anylize it in different
		digits and sum them up.
		"""

# code from others in JAVA
 1     public int digitCounts(int k, int n) {
 2         // write your code here
 3         int result = 0;
 4         int base = 1;
 5         while (n/base > 0) {
 6             int cur = (n/base)%10;
 7             int low = n - (n/base) * base;
 8             int high = n/(base * 10);
 9 
10             if (cur == k) {
11                 result += high * base + low + 1;
12             } else if (cur < k) {
13                 result += high * base;
14             } else {
15                 result += (high + 1) * base;
16             }
17             base *= 10;
18         }
19         return result;
20     }





if __name__=='__main__':
	print Solution().digitCounts(1,12)

