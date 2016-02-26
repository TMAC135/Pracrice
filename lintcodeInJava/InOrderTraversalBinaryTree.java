
//注意，此时栈和node配合使用来遍历整个树，要不然会超时或者内存溢出


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
     * @return: Inorder in ArrayList which contains node values.
     */
  
    //similar to the process of preorder, we still use stack
    //但是memory limit exceeded 和 time limit exceeded
    public ArrayList<Integer> inorderTraversal(TreeNode root) 
    {
      ArrayList<Integer> res = new ArrayList<>();
      if(root == null) return res;
      
      Stack<TreeNode> stack = new Stack<>();
      stack.push(root);
      while(!stack.empty())
      {
        TreeNode tmp = stack.peek();
        if(tmp.left == null) 
        {
          //first pop the current node and then process the right subtree
          res.add(stack.pop().val);
          
          /*又new了cur节点，没有必要
          TreeNode cur = tmp.right;
          if(cur != null)
          {
            stack.push(cur);
            while(cur.left != null)
            {
              stack.push(cur.left);
              cur = cur.left;
            }
          }
          */
          tmp = tmp.right;
          while(tmp != null)
          {
            stack.push(tmp);
            tmp = tmp.left;
          }
        }else
        {
          //if left node is not empty, we keep add node to the stack
          while(tmp.left != null)
          {
            stack.push(tmp.left);
            tmp = tmp.left;
          }          
        }//end of if else        
      }
      return res;
    }
  
      //一个node配合stack来使用，其中node代表遍历到了哪个节点
      //much simplier, 这里的root 元素就是下一步要处理的节点，因为时中序遍历，我们的root开始时尽量指向左边，
      //但是当左边为空时，我们需要将当前节点弹出，然后指向当前节点的右节点。
      public ArrayList<Integer> inorderTraversal(TreeNode root) 
    {
      ArrayList<Integer> res = new ArrayList<>();
      
      Stack<TreeNode> stack = new Stack<>();
      
      while(root != null || !stack.empty())
      {
        if(root == null)
        {
          //注意不要多次new对象，因为有可能超过内存，能用原来的变量就用原来的
          root = stack.pop();
          res.add(root.val);
          root = root.right;
        }else
        {
          stack.push(root);
          root = root.left;
        }
      }
      return res; 
    }
  
}