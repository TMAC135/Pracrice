/*
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

Example
Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].
*/

/*
这道题不仅要insert newInterval同时还要保证能够merge。那么就分情况讨论。

遍历每一个已给出的interval，

当当前的interval的end小于newInterval的start时，说明新的区间在当前遍历到的区间的后面，并且没有重叠，所以res添加当前的interval；

当当前的interval的start大于newInterval的end时，说明新的区间比当前遍历到的区间要前面，并且也没有重叠，所以把newInterval添加到res里，并更新newInterval为当前的interval； 

当当前的interval与newInterval有重叠时，merge interval并更新新的newInterval为merge后的。
*/



/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */

    //这题我准备用二分法来做，但是忽略了边界条件并不是startIndex < endIndex - 1,因为有这种情况
    //Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
	//This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) 
    {
        ArrayList<Interval> result = new ArrayList<Interval>();
        if(intervals == null || intervals.size() == 0)
        {
          if(newInterval != null)
          {
            result.add(newInterval);
          }
          return result;
        }
        
        //use binay serach 
      int startIndex = 0;
      int endIndex = intervals.size() - 1;
      Interval start = intervals.get(startIndex);
      Interval end = intervals.get(endIndex);
      if(newIntervals.end < start.start) 
      { 
        result = insertion(0,intervals);
        return result;
      }
      if(newIntervals.start > end.end) 
      {
        result = insertion(intervals.size()-1,intervals);
        return result;
      }
      
      //every time we garantee the range of newInterval is in in the range of start and end range
      while(startIndex < endIndex - 1)
      {
        Interval start = intervals.get(startIndex);
        Interval end = intervals.get(endIndex);
        int midIndex = (startIndex + endIndex) / 2;
        mid = intervals.get(midIndex);
        if(mid.left <= newInterval.left) start = mid;
        if(mid.right >= newInterval.right) end = mid;
      }
      //finally we have will end up with getting two intervals
      
      
      
      
    }
  
 	//insert the interval in the certain position 
    public static ArrayList<Interval> insertion(int index,ArrayList<Interval>)
    {
      ArrayList<Interval> result = new ArrayList<Interval>();
      
      return result;
    }
}


//别人的解法，如上述那样，依次扫描插入的newInterval 和所有 intervals,然后判断是否与他们有所重叠，再merge
public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
         ArrayList<Interval> res = new ArrayList<Interval>();
             
         for(Interval each: intervals){
             if(each.end < newInterval.start){
                 res.add(each);
             }else if(each.start > newInterval.end){
                 res.add(newInterval);
                 newInterval = each;        
             }else if(each.end >= newInterval.start || each.start <= newInterval.end){
                 int nstart = Math.min(each.start, newInterval.start);
                 int nend = Math.max(newInterval.end, each.end);
                 newInterval = new Interval(nstart, nend);
             }
         }
  
         res.add(newInterval); 
  
         return res;
     }

//我觉得的优化的解法，先用二分法将整体范围缩小，是的start.left <= newInterval.left && end.right >= newInterval.right
//然后我们再向上述方法再依次扫描，得到最终的merge后的interval再依次加入到result;





