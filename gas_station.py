# coding=utf-8

"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Example
Given 4 gas stations with gas[i]=[1,1,3,1], and the cost[i]=[2,2,1,1]. The starting gas station's index is 2.

Note
The solution is guaranteed to be unique.

Challenge
O(n) time and O(1) extra space
"""

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    """
    这一题纠结于O(n)时间复杂度了，原来以为要从每一个站开始搜索一下，因此可以O(n^2)的复杂度，
    但是其实我们可以在遍历的同时更新index 的信息，例如：
    假设我们从i 开始的，到j不满足条件了，那么我们可以得出结论在 i~j 中间任意一个站都不是这个index,
    因此我们可以更新index 到下一站。

    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
		if sum(gas) < sum(cost):
			return -1
		cur = 0
		index = 0
		for i in xrange(len(cost)):
			if cur + gas[i] < cost[i]:
				index =i+1
				cur = 0
			else:
				cur += gas[i] - cost[i]
		return index


if __name__ == '__main__':
	print Solution().canCompleteCircuit([1,1,3,1],[2,2,1,1]) 