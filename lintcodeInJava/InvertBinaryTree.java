
/* 翻转一个二叉树，或者是一个二叉树的镜像
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
*/

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
 
 //first method: do it recursively,notice the return type and the edge case
public class Solution 
{
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) 
    {
        // write your code here
        if(root == null) return;
        
        helper(root);
    }
    
    //helper function is used to invert the tree for given root node
    public TreeNode helper(TreeNode root)
    {
        //edge case
        if(root == null) return null;
        if(root.left == null && root.right == null) return root;
        
        TreeNode left = helper(root.left);
        TreeNode right = helper(root.right);
        TreeNode tmp = left;
        root.left = right;
        root.right = tmp;
        return root;
    }
}

// 第二种：看别人的方法，同样也是recursion,但是只需要一个函数,只需要五行代码
public class Solution 
{
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) 
    {
        // write your code here
        if(root == null) return;

        invertBinaryTree(root.left);
        invertBinaryTree(root.right);

        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;                
    }
}

//第三种方法：非递归的方法，类似层次遍历，需要配合queue的使用
public class Solution 
{
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) 
    {
        // write your code here
        if(root == null) return;

        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        TreeNode cur;

        while(!queue.isEmpty())
        {
        	cur = queue.poll();
        	if(cur.left == null && cur.right == null) continue;
        	else 
        	{
        		//we swap the order of left and right node 
        		TreeNode leftNode = cur.left;
        		TreeNode rightNode = cur.right;
        		TreeNode tmp = leftNode;
        		cur.left = rightNode;
        		cur.right = tmp;

        		//then we add the child nodes to the queue
        		if(cur.left != null) queue.add(cur.left);
        		if(cur.right != null) queue.add(cur.right);
        	}
        }

    }
}