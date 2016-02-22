


//别人的解法，使用hashtable 并且已经去重复
public class Solution {
public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
    final int length = num.length;
    ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
    HashMap<Integer, int[]> hashMap = new HashMap<Integer, int[]>();

    // if length is less than 3, return empty result set
    if (length < 3) return result;

    Arrays.sort(num);

    for (int i = 0; i < length - 2; i++) {
        if (num[i] > 0) break;
        hashMap.clear();

        if (i == 0 || num[i] > num[i - 1]) {
            for (int j = i + 1; j < length; j++) {
                if (hashMap.containsKey(num[j])) { // found target
                    ArrayList<Integer> elem = new ArrayList<Integer>(3);

                    elem.add(hashMap.get(num[j])[0]);
                    elem.add(hashMap.get(num[j])[1]);
                    elem.add(num[j]);

                    result.add(elem);

                    // remove duplicated elements
                    while (j < (length - 1) && num[j] == num[j + 1]) j++;
                } else {
                    int[] temp = new int[2];
                    temp[0] = num[i];
                    temp[1] = num[j];
                    hashMap.put(0 - (num[i] + num[j]), temp);
                }
            }
        }
    }
    return result;
}


//同样别人的解法，但是通过hashset来去重复的
 1     public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
 2         ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
 3         if(num.length<3||num == null)
 4             return res;
 5         
 6         HashSet<ArrayList<Integer>> hs = new HashSet<ArrayList<Integer>>();
 7         
 8         Arrays.sort(num);
 9         
10         for(int i = 0; i <= num.length-3; i++){
11             int low = i+1;
12             int high = num.length-1;
13             while(low<high){//since they cannot be the same one, low should not equal to high
14                 int sum = num[i]+num[low]+num[high];
15                 if(sum == 0){
16                     ArrayList<Integer> unit = new ArrayList<Integer>();
17                     unit.add(num[i]);
18                     unit.add(num[low]);
19                     unit.add(num[high]);
20                     
21                     if(!hs.contains(unit)){
22                         hs.add(unit);
23                         res.add(unit);
24                     }
25                     
26                     low++;
27                     high--;
28                 }else if(sum > 0)
29                     high --;
30                  else
31                     low ++;
32             }
33         }
34         
35         return res;
36     }