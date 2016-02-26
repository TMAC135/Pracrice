

/*
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Note
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters
*/

/*
我的刚开始的想法，想利用DP 来解决问题，但是不知从何下笔
*/

/*
别人的解法：将其联系到图的算法中：
这道题看似一个关于字符串操作的题目，其实要解决这个问题得用图的方法。我们先给题目进行图的映射，顶点则是每个字符串，
然后两个字符串如果相差一个字符则我们进行连边。接下来看看这个方法的优势，注意到我们的字符集只有小写字母，
而且字符串长度固定，假设是L。那么可以注意到每一个字符可以对应的边则有25个（26个小写字母减去自己），
那么一个字符串可能存在的边是25*L条。接下来就是检测这些边对应的字符串是否在字典里，就可以得到一个完整的图的结构了。
根据题目的要求，等价于求这个图一个顶点到另一个顶点的最短路径，一般我们用广度优先搜索（不熟悉搜索的朋友可以看看Clone Graph）即可。
这个算法中最坏情况是把所有长度为L的字符串都看一下，或者把字典中的字符串都看一下，而长度为L的字符串总共有26^L，
所以时间复杂度是O(min(26^L, size(dict))，空间上需要存储访问情况，也是O(min(26^L, size(dict))。
*/

public int ladderLength(String start, String end, HashSet<String> dict) {  
    if(start==null || end==null || start.length()==0 || end.length()==0 || start.length()!=end.length())  
        return 0;  
    LinkedList<String> queue = new LinkedList<String>();  
    HashSet<String> visited = new HashSet<String>();  
    int level= 1;  //level代表我们bfs已经深入的层数
    int lastNum = 1;  //lastNum表示我们已经处理的元素，他和curNum配合使用以便于我们知道我们什么时候来更新level的大小
    int curNum = 0;  
    queue.offer(start);  
    visited.add(start);  
    while(!queue.isEmpty())  
    {  
        String cur = queue.poll();  
        lastNum--;  
        for(int i=0;i<cur.length();i++)  
        {  
            char[] charCur = cur.toCharArray();  
            for(char c='a';c<='z';c++)  
            {  
                charCur[i] = c;  
                String temp = new String(charCur);  
                if(temp.equals(end))  
                    return level+1;  
                if(dict.contains(temp) && !visited.contains(temp))  
                {  
                    curNum++;  
                    queue.offer(temp);  
                    visited.add(temp);  
                }  
            }  
        } 
        //当lastNum 为0时，代表我们上个level的节点已经处理完了，我们更新下一层的节点数 
        if(lastNum==0)  
        {  
            lastNum = curNum;  
            curNum = 0;  
            level++;  
        }  
    }  
    return 0;  
}