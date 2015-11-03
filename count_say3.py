class Solution(object):
	def countandsay(self,n):
		ans=''
		if n==1:
			ans='1'
			return ans
		elif n==2:
			return '11'
		last='11'
		for jj in xrange(3,n+1):
			count=1
			ans=''
			for  ii,c in enumerate(last[1:]):
				if c==last[ii-1]:
					count+=1
				else:
					ans=str(count)+last[ii-1]
					count=1
		last=ans
		return ans
			




