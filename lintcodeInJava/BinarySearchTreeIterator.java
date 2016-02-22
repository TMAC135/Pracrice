

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/*
1: brute force solution, store the in order traversal into a ArrayList
2: But is is memory cost
*/

/*
总结一下，其实这题就是将in-order traversal的代码放在了next()方法里面：
再次回顾一下，中序遍历，注意对于每个从栈中弹出的元素，如果该元素有右节点，那么就从该节点的右节点开始
再次向stack里面push元素，判断结束的条件是stack为空，
*/
//我的解法，有bug,看了别人的解法，修复了bug
public class BSTIterator 
{
    private Stack<TreeNode> stack = new Stack<TreeNode>();
    public BSTIterator(TreeNode root) 
    {
      //we first construct the stack with the root node
      while(root != null)
      {
          stack.push(root);
          root=root.left;
      }
        
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() 
    {
      if(stack.empty()) return false;
      else return true;        
    }

    /** @return the next smallest number */
    public int next() 
    {
      if(!hasNext()) return 0;
      TreeNode leftNode = stack.pop();
      if(stack.empty() && leftNode.right == null) return leftNode.val;
      if(leftNode.right != null) helper(leftNode);
      //不需要此判断条件，因为对于每个节点，如果我们
      // else 
      // {
      //   TreeNode parent = stack.pop();
      //   helper(parent);
      //   stack.push(parent);
      // }
      return leftNode.val;
    }
    //this function is used to fill in more element into the stack from the current node 
    //to the left most of the nodes in thes subtree.
    private void helper(TreeNode node)
    {
      TreeNode root = node.right;
      while(root != null)
      {
        stack.push(root);
        root = root.left;
      }
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */


//别人的解法
//1:brute force,用递归创建整个树的in-order-traversal,然后再用index来表示访问的元素


 1 /*
 2  * Definition for binary tree
 3  * public class TreeNode {
 4  *     int val;
 5  *     TreeNode left;
 6  *     TreeNode right;
 7  *     TreeNode(int x) { val = x; }
 8  * }
 9  */
 
 public class BSTIterator {
     ArrayList<TreeNode> list;
     int index;
 
     public BSTIterator(TreeNode root) {
         list = new ArrayList<TreeNode>();
         iterator(root, list);
         
         index = 0;
     }
     
     // solution 1: recursion.
     public void dfs (TreeNode root, ArrayList<TreeNode> ret) {
         if (root == null) {
             return;
         }
         
         //Use inorder traversal.
         dfs(root.left, ret);
         ret.add(root);
         dfs(root.right, ret);
     }
     
    
     /** @return whether we have a next smallest number */
     public boolean hasNext() {
         if (index < list.size()) {
             return true;
         }
         
         return false;
     }
 
     /** @return the next smallest number */
     public int next() {
         return list.get(index++).val;
     }
 }

//别人的解法2
//思路跟我的差不多
/*
这是一道很经典的题目，考的非递归的中序遍历。其实这道题等价于写一个二叉树中序遍历的迭代器。需要内置一个栈，一开始先存储到最左叶子节点的路径。
在遍历的过程中，只要当前节点存在右孩子，则进入右孩子，存除从此处开始到当前子树里最左叶子节点的路径。
*/
 public class BSTIterator {  
    Stack<TreeNode> stack;  
  
    public BSTIterator(TreeNode root) {  
        stack = new Stack<TreeNode>();  
        while (root != null) {  
            stack.push(root);  
            root = root.left;  
        }  
    }  
  
    /** @return whether we have a next smallest number */  
    public boolean hasNext() {  
        return !stack.isEmpty();  
    }  
  
    /** @return the next smallest number */  
    public int next() {  
        TreeNode node = stack.pop();  
        int ret = node.val;  
        if (node.right != null) {  
            node = node.right;  
            while (node != null) {  
                stack.push(node);  
                node = node.left;  
            }  
        }  
        return ret;  
    }  
}



