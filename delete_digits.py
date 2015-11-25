# coding=utf-8

"""
Given string A representative a positive integer which has N digits, 
remove any k digits of the number, the remaining digits are arranged
according to the original order to become a new positive integer.

Find the smallest integer after remove k digits.
N <= 240 and k <= N,

Example
Given an integer A = "178542", k = 4

return a string "12"

"""

"""
From other's notes:
这道题跟Leetcode里面的那道Next Permutation很像，那个题要找比一个数大的下一个数，于是从这个数的右边开始，
找第一个递减的位置所在。这道题也是类似，只不过从这个数的左边开始，找第一个递减的位置所在。
那道题是想要改动的影响最小，所以从右边开始扫描。这道题是想要改动的影响最大，所以从左边开始扫描。
这道题，删掉一个数，相当于用这个数后面的数代替这个数。所以后面这个数一定要比当前小才行。所以找的是第一个递减的位置，把大的那个数删了。

这样做一次就是找到了：删除哪一个数，使得剩下的数最小。对剩下的数再做k次，就可以找到删除哪k个数，使得剩下的数最小。这其实是一个Greedy算法，因为这样每做一次，得到的都是当前最优的结果。
看起来需要O(Nk)时间复杂度，但其实用一个Stack，再记录pop了几次，O(2N)就好了


可能一开始想到的是DFS暴力枚举，但是N大小为240显然暴力的方法并不可取。
仔细想想发现其实还是很容易找到规律的，想让一个数字尽可能小，那么就要把小的数字尽量放到前面，
如果前面有比它大的数字，那么就到把在它前面且比它大的数字都要删除掉，直到已经删掉k个数字。剩下的就是一些特殊情况与边界情况了，
比如前置0要去掉，如果遍历一遍发现删除的数字还不足k个，那么就把最后的k-cnt个删除掉。下面是AC的代码
"""

class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string

    should ask the interviewer the case that 0 occur in the front part of the string like
    '00001078642' k=4, 

    """
    def DeleteDigits(self, A, k):
        # write you code here
        if not A:
        	return ""
        res = ''
        count = 0
        for i in A:
        	# this is used to iterative judge the current element and the elements in the res
        	while (res != '' and count < k):
        		if res[-1] > i:
	        		res = res[:-1]
	        		count += 1
	        		# if i == '0' and len(res) == 1:
	        		# 	break
	        		# else:
	        		# 	res = res[:-1]
	        		# 	count += 1
	        	else:
	        		break
	    # this is used to eliminate the case where the first character is not 0
        	if i != '0' or res:
        		res += i
        if count < k:
        	res = res[:-(k-count)]
        return res


if __name__ == '__main__':

	print Solution().DeleteDigits('001078642',4)


