/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/*
any order requirements in the list?
*/
public class Solution 
{
    public List<String> binaryTreePaths(TreeNode root) 
    {
        ArrayList<String> res = new ArrayList<>();
        if(root == null) return res;
        String path = Integer.toString(root.val);
        helper(root,res,path);
        return res;
      
    }
  
    //树递归一定要遵循三个步骤：
    //1:what do you do for the left and right child?(base condition,what's the return type, usually the same as function)
    //2:how to handle with current node
    //3:what does parent node expect?
    public static void helper(TreeNode root,List<String> res,String path)
    {
      // String newPath = path + "->" + Integer.toString(root.val);
      if(root.left == null && root.right == null)
      {
        res.add(path);
      }
      if(root.left != null)
      {
        helper(root.left,res,path + "->" + Integer.toString(root.left.val));
      }
      if(root.right != null)
      {
        helper(root.right,res,path + "->" + Integer.toString(root.right.val));
      }
    }

}

/*
下面两种解法都是有两个容器，一个装string,一个装node,然后同时push或者pop,保证一致性
*/
//BFS 解法
public class Solution {
//BFS - Queue
public List<String> binaryTreePaths(TreeNode root) {
    List<String> list=new ArrayList<String>();
    Queue<TreeNode> qNode=new LinkedList<TreeNode>();
    Queue<String> qStr=new LinkedList<String>();

    if (root==null) return list;
    qNode.add(root);
    qStr.add("");
    while(!qNode.isEmpty()) {
        TreeNode curNode=qNode.remove();
        String curStr=qStr.remove();

        if (curNode.left==null && curNode.right==null) list.add(curStr+curNode.val);
        if (curNode.left!=null) {
            qNode.add(curNode.left);
            qStr.add(curStr+curNode.val+"->");
        }
        if (curNode.right!=null) {
            qNode.add(curNode.right);
            qStr.add(curStr+curNode.val+"->");
        }
    }
    return list;
}


//DFS解法
public class Solution {
//DFS - Stack
public List<String> binaryTreePaths(TreeNode root) {
    List<String> list=new ArrayList<String>();
    Stack<TreeNode> sNode=new Stack<TreeNode>();
    Stack<String> sStr=new Stack<String>();

    if(root==null) return list;
    sNode.push(root);
    sStr.push("");
    while(!sNode.isEmpty()) {
        TreeNode curNode=sNode.pop();
        String curStr=sStr.pop();

        if(curNode.left==null && curNode.right==null) list.add(curStr+curNode.val);
        if(curNode.left!=null) {
            sNode.push(curNode.left);
            sStr.push(curStr+curNode.val+"->");
        }
        if(curNode.right!=null) {
            sNode.push(curNode.right);
            sStr.push(curStr+curNode.val+"->");
        }
    }
    return list;
}
