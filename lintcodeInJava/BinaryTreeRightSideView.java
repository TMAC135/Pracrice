

/* Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4]
*/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


//clarifications: what if the root is null
/*
分析，首先，因为是输出每一层最靠右的元素，我们是不能直接通过一次 pass来得到结果的，我们需要记录每一层的元素
节点，而且需要该层的节点来得到下一层的节点内容
*/


//first idea: similar to the level order travesal, but we only track the rightmost element
//but memory limit exceed
public class Solution 
{
    public List<Integer> rightSideView(TreeNode root) 
    {
      ArrayList<Integer> res = new ArrayList<>();
      
      //special case
      if(root == null) return res;
      
      LinkedList<TreeNode> queue = new LinkedList<>();
      queue.add(root);
      // int rightMost;
      
      while(!queue.isEmpty())
      {
        //first add the last element from the queue
        res.add(queue.get(queue.size() -1 ).val);
        
        LinkedList<TreeNode> next = new LinkedList<>();
        // TreeNode tmp;
        while(!queue.isEmpty())
        {
          next.add(queue.poll());          
        }
        queue = next;
      }
      
      return res;
        
    }
}

//别人的解法，用queue的结构特点来解决，但是当当前节点没有子节点时，我们处理其sibling,但是注意要往里面加一个null
//解法非常巧妙，用null来标记每一层，例如：
/*
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

栈的存贮情况是: [1,null,2,3,null,5,4,null]
*/


public class Solution {  
    public List<Integer> rightSideView(TreeNode root) {  
        List<Integer> ans = new ArrayList<Integer>();  
        if (root == null) return ans;  
          
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();  
        queue.add(root);  
        queue.add(null);  
          
        while (!queue.isEmpty()) {  
            TreeNode node = queue.pollFirst();  
              
            if (node == null) {  
                if (queue.isEmpty()) {  
                    break;  
                } else {  
                    queue.add(null);  
                }  
            } else {  
                // add the rightest to the answer  
                if (queue.peek() == null) {  //当我们瞥一眼的结果是null，那么则表明现在的元素就是当层最靠右的元素
                    ans.add(node.val);  
                }  
                  
                if (node.left != null) {  
                    queue.add(node.left);  
                }  
                if (node.right != null) {  
                    queue.add(node.right);  
                }  
            }  
        }  
          
        return ans;  
    }  
}





//second method, try to solve it in dfs, we are add the element when we pass through the tree
//没做出来，卡在了如何遍历树
public class Solution {
    public List<Integer> rightSideView(TreeNode root) 
    {
      ArrayList<Integer> res = new ArrayList<>();
      
      if(root == null) return res;
      
      TreeNode cur = root;
      
      while(cur != null)
      {
        res.add(cur.val);
        
        if(cur.right != null)
        {
          cur = cur.right;
        }else
        {
          cur = cur.left;
        }
      }
      return res;
    }
}

 //别人的答案：首先用一个hashmap记录，key是层数，value是最右边的值，
//巧妙的就是先从左边遍历，然后向右遍历，覆写原来的值
public class Solution {
    private void dfs(HashMap<Integer, Integer> depthToValue, TreeNode node, int depth) {
        if (node == null) {
            return;
        }
        
        depthToValue.put(depth, node.val);
        dfs(depthToValue, node.left, depth + 1);
        dfs(depthToValue, node.right, depth + 1);
    }
    
    public List<Integer> rightSideView(TreeNode root) {
        HashMap<Integer, Integer> depthToValue = new HashMap<Integer, Integer>();
        dfs(depthToValue, root, 1);
        
        int depth = 1;
        List<Integer> result = new ArrayList<Integer>();
        while (depthToValue.containsKey(depth)) {
            result.add(depthToValue.get(depth));
            depth++;
        }
        return result;
    }
}