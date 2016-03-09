/*
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level)
eg:
	3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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

import java.util.*;
public class BinaryTreeLevelOrderTraversal 
{
	//我的第一种方法，使用arraylist,思路是正确的，但不工作
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) 
    {
    	if (root == null) return null;
    	//store the final result
    	ArrayList result = new ArrayList();
    	//store the values of every level 
    	List<Integer> levelValues = new ArrayList<Integer>();
    	// the queue we use to iterate the level nodes
    	List<TreeNode> level = new ArrayList<TreeNode>();
    	level.add(root);

    	while(level != null)
    	{
    		/*
    		第一遍的错误做法，因为增强for循环是随机的在容器内选择元素
    		*/
    		// for(TreeNode node:level)
    		// {
    		// 	if(node.left != null)
    		// 	{ 
    		// 		next.add(node.left);
    		// 		levelValues.add(node.left.val);
    		// 	}
    		// 	if(node.right != null) 
    		// 	{
    		// 		next.add(node.right);
    		// 		levelValues.add(node.right.val);
    		// 	}
    		// }
    		List<TreeNode> next = new ArrayList<TreeNode>();//to keep track the next level nodes

    		for(int i=0;i<level.size();i++)
    		{
    			TreeNode tmp = level.get(i);
    			levelValues.add(tmp.val);
    			if(tmp.left != null) next.add(tmp.left);
    			if(tmp.right != null) next.add(tmp.right)
    		}
    		// update the level
    		level = next;
    		next.clear();
    		//append the values and clear for the next iteration
    		result.add(levelValues);
    		levelValues.clear();
    	}

    	return result;
        
    }

//方法2:使用queue来解决，看过别人代码后,这种方法是bfs,每次将每层的值打印出来
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList result = new ArrayList();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            ArrayList<Integer> level = new ArrayList<Integer>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode head = queue.poll();
                level.add(head.val);
                if (head.left != null) {
                    queue.offer(head.left);
                }
                if (head.right != null) {
                    queue.offer(head.right);
                }
            }
            result.add(level);
        }

        return result;
    }



    // print 出来 BST 每一层，一层一行，逗号空格分开
    public void print(TreeNode root)
    {

    }
}

//方法3:思想类似于Binary Tree Right Side View（199）这道题，我们使用queue,然后用null来分割每层，
// 当我们遇到null时，append这个list,这样我们就不用每次new出新的ArrayList了
/*
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

栈的存贮情况是: [1,null,2,3,null,5,4,null]
*/

