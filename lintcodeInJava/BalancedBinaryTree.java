

/*
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1

Example
Given binary tree A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
*/


//解法1:naive 解法，递归求到每棵树的左右节点的的高度，然后在从上到下依次判断
//这种方法因为重复访问了每个节点，效率将会非常低


//解法2:后序遍历整个树(left -> right -> current)，并且递归的函数返回值有两个，一个是boolean,判断是否是平衡的，第二个是
//该树的高度，由于java是按值传递的，为了达到这种效果，我们需要自定义一种数据类型，ResultType，包括
//boolean 和 int,

class ResultType {
    public boolean isBalanced;
    public int maxDepth;
    public ResultType(boolean isBalanced, int maxDepth) {
        this.isBalanced = isBalanced;
        this.maxDepth = maxDepth;
    }
}

public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root) {
        return helper(root).isBalanced;
    }
    
    private ResultType helper(TreeNode root) {
        if (root == null) {
            return new ResultType(true, 0);
        }
        
        ResultType left = helper(root.left);
        ResultType right = helper(root.right);
        
        // subtree not balance
        if (!left.isBalanced || !right.isBalanced) {
            return new ResultType(false, -1);
        }
        
        // root not balance
        if (Math.abs(left.maxDepth - right.maxDepth) > 1) {
            return new ResultType(false, -1);
        }
        
        return new ResultType(true, Math.max(left.maxDepth, right.maxDepth) + 1);
    }
}


// 解法3:因为树的高度肯定 >= 0，当遇到不平衡的树时，我们可以将其高度设为－1，这样我们
//就可以省掉一个boolean的返回类型，只需要判断树的高度是否为－1就可以判断该树是否平衡

public class Solution
{

	public boolean isBalanced(TreeNode root)
	{

		int res = getHeight(root);
		return res == -1 ? false : true;
	}

	public int getHeight(TreeNode root)
	{
		if(root == null) return 0;

		int left = getHeight(root.left);
		int right = getHeight(root.right);

		if(left == -1 || right == -1 || Math.abs(left-right) > 1) return -1;
		else return Math.max(left,right) + 1;
	}


}