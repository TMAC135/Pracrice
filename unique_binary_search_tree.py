#coding=utf-8
"""
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3


"""
# 用dp 只求数量问题
class Solution:
    # @paramn n: An integer
    # @return: An integer

    """
    the status equation for this problem is
    dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+......+dp[n-1]*dp[0]

    if we want to list the binary trees, we need to use dfs to 
    travel the tree.
    see unique_binary_search_treeII.py
    """
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n-2)]
            for i in range(3, n + 1):
                for j in range(1, i+1):
                    dp[i] += dp[j-1] * dp[i-j]
            return dp[n]




if __name__=='__main__':
	print Solution().numTrees(4)