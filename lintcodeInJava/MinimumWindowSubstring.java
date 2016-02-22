

/*
Given a string source and a string target, find the minimum window in source which will contain all the characters in target

Example
For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"

Note
If there is no such window in source that covers all characters in target, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.
*/


//1: O(n^2) 的做法，两个for loop





//2:O(n)的解法，用hashmap做，我卡在了怎么寻找最小长度的substring,这是别人的分析：
/*
这道题也是用滑动窗口的思想，思想跟 Substring with Concatenation of All Words是一样的，同样是利用HashMap来存Dict，然后来遍历整个母串。因为这里是要求最短的包含子串的字符串，所以中间是可以允许有非子串字符的，当遇见非子串字符而count又没到子串长度时，可以继续走。

当count达到子串长度，说明之前遍历的这些有符合条件的串，用一个pre指针帮忙找，pre指针帮忙找第一个在HashMap中存过的，并且找到后给计数加1后的总计数是大于0的，判断是否为全局最小长度，如果是，更新返回字符串res，更新最小长度，如果不是，继续找
*/

/*
我的总结：
1: target 的hashmap 模版－－dict, 因为题目不要求按顺序的子串，因此hashmap中的
value就相当于我们要考虑的多少个字符.注意value也可以为负数，代表我们有多余的该字符，
value为正数，代表我们好需要该数目的字符来匹配，value为0时，代表我们数目正好。
2:要配合count 来记录我们实现了匹配target多少个字符，当 count == target.length时，代表我们已经
肯定找到了相应的模版，
3: pre的使用配合找出最短的子字符串，注意pre扫描的时候我们是将value＋1，
*/


 1 public String minWindow(String S, String T) {
 2     String res = "";
 3     if(S == null || T == null || S.length()==0 || T.length()==0)
 4         return res;
      
 	//key: 字符， value: 字符出现的次数，
 6     HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
 7     for(int i =0;i < T.length(); i++){
 8         if(!dict.containsKey(T.charAt(i)))
 9             dict.put(T.charAt(i), 1);
10         else
11             dict.put(T.charAt(i), dict.get(T.charAt(i))+1);
12     }
13     
14     int count = 0;
15     int pre = 0;
16     int minLen = S.length()+1;
17     for(int i=0;i<S.length();i++){
18         if(dict.containsKey(S.charAt(i))){
19             dict.put(S.charAt(i),dict.get(S.charAt(i))-1);
20             if(dict.get(S.charAt(i)) >= 0)
21                 count++;
22                 
23             while(count == T.length()){
24                 if(dict.containsKey(S.charAt(pre))){
25                     dict.put(S.charAt(pre),dict.get(S.charAt(pre))+1);
26                     

27                     if(dict.get(S.charAt(pre))>0){
28                         if(minLen>i-pre+1){
29                             res = S.substring(pre,i+1);
30                             minLen = i-pre+1;
31                         }
32                         count--;
33                     }
34                 }
35                 pre++;
36             }
37         }//end for if(dict.containsKey(S.charAt(i)))
38     }
39     return res;
40 }