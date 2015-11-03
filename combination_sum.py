# Given a set of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
#Given a set of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.

# for example, given candidate set 2,3,6,7 and target 7, 
#A solution set is: 
#[7] 
#[2, 2, 3]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        if target < 0 or not candidates:
        	return []
        candidates.sort()
        if candidates[0] > target:
        	return []
        result = []
        for i in range(len(candidates)):
        	if candidates[i] == target:
        		result.append([target])
        	if solve(candidates,target-candidates[i]) == []:
        		continue
        	else:
        		result.extend(solve(candidates,target-candidates[i]))
        return result






    def solve(self,candidates,target):

    	for i in range(len(candidates)):
    		 
