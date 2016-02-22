


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
public class Solution 
{
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in ArrayList which contains node values.
     */

// pre-order of binary tree - non recursion method - work with stack
    public ArrayList<Integer> preorderTraversal(TreeNode root) 
    {
      ArrayList<Integer> res = new ArrayList<>();
      Stack<TreeNode> stack = new Stack<TreeNode>();
      if(root == null) return res;
      stack.push(root);
      while(!stack.empty())
      {
        TreeNode pop = stack.pop();
        res.add(pop.val);
        if(pop.right != null) stack.push(pop.right);
        if(pop.left != null) stack.push(pop.left);
      }
      return res;
      
    }
}