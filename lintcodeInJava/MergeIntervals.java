/*
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
*/

// copy from others, 

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
 
/*
some classifications for this problem:
1: are all intervals given are valid? 
2: how about the case where two intervals has the leftBound = rightBound, like [1,2],[2,3]
3: Can we use the sort function in the Collections module.
*/

public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
           if (intervals == null || intervals.size() <= 1)
              return intervals;
   
          // sort intervals by using self-defined Comparator
          Collections.sort(intervals, new IntervalComparator());
   
          ArrayList<Interval> result = new ArrayList<Interval>();
   
   		//根据已排好序的list，依次遍历每个元素，进行合并
         Interval prev = intervals.get(0);
         for (int i = 1; i < intervals.size(); i++) {
             Interval curr = intervals.get(i);
  
             if (prev.end >= curr.start) {
                 // merged case
                 Interval merged = new Interval(prev.start, Math.max(prev.end, curr.end));
                 prev = merged;
             } else {
                 result.add(prev);
                 prev = curr;
             }
         }
  
         result.add(prev);
  
         return result;
         }
     }
  
  	//此题的重点是重写comparator函数来对原list进行排序，排序的规则是根据左边节点的大小，这边我们默认
     // 所有的interval都是合理的
     class IntervalComparator implements Comparator<Interval> {
         public int compare(Interval i1, Interval i2) {
             return i1.start - i2.start;
         }
}