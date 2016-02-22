

//别人的解法1:虽然得到了结果，但是破坏了原来树的结构
/*
开一个Stack，由于root结点是最后访问的结点，所以我们先将root结点push到Stack中

我们写一个while循环，while循环结束的条件是栈中没有任何结点。

当栈中有结点的时候，我们将取出栈顶结点

1、判断下它是否是叶子结点（left和right都为null）, 如果是叶子结点的话，那么不好意思，把它弹出栈，并把值add到ArrayList中，如果不是叶子结点的话，那么

2、我们判断下它的left（node.left）是否为null,如果不为null，把它的左孩子结点push到栈中来，并把它的左孩子域设为null, 然后跳过此次循环剩下的部分

3、如果它的left 为null, 把它的右孩子结点push到栈中来，并把它的右孩子域设为null，然后跳过此次循环剩下的部分！
*/

import java.util.ArrayList;  
import java.util.Stack;  
  
  
class TreeNode {  
    int val;  
    TreeNode left;  
    TreeNode right;  
  
    TreeNode(int x) {  
        val = x;  
    }  
}  
public class Solution {  
      
    public ArrayList<Integer> postorderTraversal(TreeNode root) {  
        if (root == null)  
            return null;  
        ArrayList<Integer> list = new ArrayList<Integer>();  
        Stack<TreeNode> stack = new Stack<TreeNode>();  
        //先把最后访问的结点先放入到栈中，即根节点root  
        stack.push(root);  
        while (stack.size() != 0){  
            TreeNode top = stack.peek();  
            if (top.left == null && top.right == null){  
                list.add(top.val);  
                stack.pop();  
            } 

            //解决了我遇到的问题：再向栈中加元素的时候，我们的判断程序会不断循环，但是当
            //我们在加元素后重新设置left和right的值的话，就不会有这种情况 
            if (top.left != null){  
                stack.push(top.left);  
                top.left = null;  
                continue;  
            }  
            if (top.right != null){  
                stack.push(top.right);  
                top.right = null;  
                continue;  
            }  
        }  
        return list;  
    }  
}



/*
别人的解法2：recursive way and iterative way
*/

//Recursive
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();

    if (root == null) {
        return result;
    }

    result.addAll(postorderTraversal(root.left));
    result.addAll(postorderTraversal(root.right));
    result.add(root.val);

    return result;   
}


//注意这种方法，类似于pre order,但是我们需要prev来判断上个处理的节点和现在处理的节点的关系，
//以便于我们traverse down/up fromthe tree
//Iterative
public ArrayList<Integer> postorderTraversal(TreeNode root) {
    ArrayList<Integer> result = new ArrayList<Integer>();
    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode prev = null; // previously traversed node
    TreeNode curr = root;

    if (root == null) {
        return result;
    }

    stack.push(root);
    while (!stack.empty()) {
        curr = stack.peek();
        if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
            if (curr.left != null) {
                stack.push(curr.left);
            } else if (curr.right != null) {
                stack.push(curr.right);
            }
        } else if (curr.left == prev) { // traverse up the tree from the left
            if (curr.right != null) {
                stack.push(curr.right);
            }
        } else { // traverse up the tree from the right
            result.add(curr.val);
            stack.pop();
        }
        prev = curr;
    }

    return result;
}
















