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
     * @return: An integer.
     */
    //simple recursion method, 
    public int minDepth(TreeNode root) 
    {
    	if(root == null)return 0;
    	if(root.left == null && root.right == null) return 1;

    	if (root.left == null) return minDepth(root.right) + 1;
    	else if(root.right == null) return minDepth(root.left) + 1; 
    	else return Math.min(minDepth(root.right) + 1,minDepth(root.left) + 1 );
    }

    //how is the case where the left sub tree is much deeper than right subtree, how to optimize that?
    //my solution: use queue to store the nodes for every level, than we just need to check evry node for each level.
}

public class Solution {
    public int minDepth(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
       if(root==null) return 0;
       
       ArrayList<TreeNode> last =new ArrayList<TreeNode>();
       last.add(root);
       int count=1;
       while(!last.isEmpty()){           
        ArrayList<TreeNode> curr = new ArrayList<TreeNode>();
        for(TreeNode n:last){
           if(n.left==null && n.right==null) return count;
           if(n.left!=null) curr.add(n.left);
           if(n.right!=null) curr.add(n.right);
        }
        count++;
        last=new ArrayList<TreeNode>(curr);
       }
       return count;
    }
}