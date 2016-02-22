

/*
 Construct Binary Tree from Inorder and Postorder Traversal
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
 


 /*例子：
        1
      2   3
    7 8  4 5
            6  
In-order: [7,2,8,1,4,3,5,6]
post-order: [7,8,2,4,6,5,3,1]

每次递归是in order和post order的数组都是该子树的前序和后续遍历，这样就比较好理解了
*/
 
public class Solution {
    /**
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
  public TreeNode buildTree(int[] inorder, int[] postorder) 
    {
      if(inorder == null || postorder == null || 
         inorder.length == 0 || postorder.length == 0) return null;
      
      int length = inorder.length;
      int target = postorder[length-1];
      // TreeNode root = new TreeNode(target);
      // int index = findIndex(inorder,0,inorder.length,int target);
      TreeNode root = helper(inorder,0,length-1,postorder,0,length-1);
      return root;
    }
  
  
    //find the first index of target happened in the given array
    public int findIndex(int[] inorder, int start, int end,int target)
    {
      for(int i=start;i <= end;i++)
      {
        if(inorder[i] == target) return i;
      }
      //the case where we could't find the target
      return 0;
    }
  
    
    //花了近一个小时搞清楚了递归传递的参数，对于这样的题，建议根据一个test case来写代码，
    //inorder 和 postorder数组都需要制定范围，这样才能有意义，debug了好久
    public TreeNode helper(int[] inorder,int inStart, int inEnd, int[] postorder,int postStart,int postEnd)
    {
      //base case
    //   if(start > end || start < 0 || end >= inorder.length) return null;
    //   if(start == end) return new TreeNode(inorder[start]);
        if(inStart > inEnd || postStart > postEnd) return null;
      
      int target = postorder[postEnd];
      TreeNode root = new TreeNode(target);
      int index = findIndex(inorder,inStart,inEnd,target);
      
      root.left = helper(inorder,inStart,index-1,postorder,postStart,postStart+index-inStart-1);
      root.right = helper(inorder,index+1,inEnd,postorder,postStart+index-inStart,postEnd-1);
      
      
      return root;
  
    }
}