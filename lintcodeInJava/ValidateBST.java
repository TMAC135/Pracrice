

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */

    // 我的第一遍解法，错误的因为只比较了父节点和左右子结点的关系，而正确的做法是
    // 将每个节点比左子树最大值大且比右子树最小值还小
    //事实上最好的递归方法就是将每个节点的范围也递归下去，如方法2
    public boolean isValidBST(TreeNode root) 
    {
    	if(root == null) return true;

    	return helper(root);

    }

    private static boolean helper(TreeNode root)
    {

    	if(root.left == null && root.right == null) return true;
    	else if(root.left == null) return (root.val <= root.right.val) && (helper(root.right));
    	else if(root.right == null) return (root.val >= root.left.val) && (helper(root.left));
    	else return (root.val <= root.right.val) && (helper(root.right)) && (root.val >= root.left.val) && (helper(root.left));

    }
}


// 方法2:answer from others, 我们找到每个节点的有效范围，然后判断该节点是否在该范围内
public boolean isValidBST(TreeNode root) {
    return isValidBST(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);    
}
 
public boolean isValidBST(TreeNode p, double min, double max){
    if(p==null) 
        return true;
 
    if(p.val <= min || p.val >= max)
        return false;
 
    return isValidBST(p.left, min, p.val) && isValidBST(p.right, p.val, max);
}

//iterative way

