
/*
题目：

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.

*/

/*
这题的难点就是如何设置hashmap中ey值，由题意可知，相同的shif pattern的字符串是一类，如：
["eqdf", "qcpr"]。

((‘q’ - 'e') + 26) % 26 = 12, ((‘d’ - 'q') + 26) % 26 = 13, ((‘f’ - 'd') + 26) % 26 = 2

((‘c’ - 'q') + 26) % 26 = 12, ((‘p’ - 'c') + 26) % 26 = 13, ((‘r’ - 'p') + 26) % 26 = 2

所以"eqdf"和"qcpr"是一组shifted strings。

*/



/*java解法：
在java中，我们最常用的是key的type是string,因此我们可以先计算相邻字符的偏移值，然后
用string来保存这些偏移值。
*/
public class Solution {  
    public List<List<String>> groupStrings(String[] strings) {  
        List<List<String>> result = new ArrayList<List<String>>();  
        HashMap<String, List<String>> d = new HashMap<>();  
        for(int i = 0; i < strings.length; i++) {  
            StringBuffer sb = new StringBuffer();  
            for(int j = 0; j < strings[i].length(); j++) {  
                sb.append(Integer.toString(((strings[i].charAt(j) - strings[i].charAt(0)) + 26) % 26));  
                sb.append(" ");  
            }  
            String shift = sb.toString();  
            if(d.containsKey(shift)) {  
                d.get(shift).add(strings[i]);  
            } else {  
                List<String> l = new ArrayList<>();  
                l.add(strings[i]);  
                d.put(shift, l);  
            }  
        }  
          
        for(String s : d.keySet()) {  
            Collections.sort(d.get(s));  
            result.add(d.get(s));  
        }   
        return result;  
    }  
}


/*
python解法：
由于python中tuple是immutable的，因此可以用tuple来当key

再次体现了python语言的简洁性
*/

class Solution(object):  
    def groupStrings(self, strings):  
        """ 
        :type strings: List[str] 
        :rtype: List[List[str]] 
        """  
        d = collections.defaultdict(list)  
        for s in strings:  
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])  
            d[shift].append(s)  
          
        return map(sorted, d.values()) 


