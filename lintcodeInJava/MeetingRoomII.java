

/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
*/


//解法必须都用到最小堆：
/*
具体思路是： 首先都原数组进行排序（根据start 值从小到大进行排序），然后我们将依次遍历
排序后的数组，并且我们将每次维护end值形成的最小堆，每次poll一个最小的end值，然后和当前的
start 值比较，如果比其小，说明rooms不需要加1，但是如果比其大，则room++
*/

//注意：如果我们每次都要拿到原来的存储数据的最小值或最大值，我们应该往heap中考虑


//下面是java和python中的堆的实现，默认都是最小堆


/** 
 * Definition for an interval. 
 * public class Interval { 
 *     int start; 
 *     int end; 
 *     Interval() { start = 0; end = 0; } 
 *     Interval(int s, int e) { start = s; end = e; } 
 * } 
 */  
import java.util.Arrays;   
   
public class Solution {  
    public int minMeetingRooms(Interval[] intervals) {  
        Arrays.sort(intervals, new IntervalComparator());  
        PriorityQueue<Integer> minHeap = new PriorityQueue();  
        int rooms = 0;  
        for(int i = 0; i < intervals.length; i++) {  
            if(minHeap.size() == 0) {  
                minHeap.add(intervals[i].end);  
                rooms++;  
                continue;  
            }  
            if(minHeap.peek() <= intervals[i].start) {  
                minHeap.poll();  
                minHeap.add(intervals[i].end);  
            } else {  
                minHeap.add(intervals[i].end);  
                rooms++;  
            }  
        }  
        return rooms;  
    }  
}  
  
class IntervalComparator implements Comparator<Interval> {  
    public int compare(Interval a, Interval b) {  
        return a.start - b.start;  
    }  
} 


# Definition for an interval.  
# class Interval(object):  
#     def __init__(self, s=0, e=0):  
#         self.start = s  
#         self.end = e  
import heapq  
  
class Solution(object):  
    def minMeetingRooms(self, intervals):  
        """ 
        :type intervals: List[Interval] 
        :rtype: int 
        """  
        heap, num = [], 0  
        heapq.heapify(heap)  
        intervals.sort(lambda a, b : a.start - b.start)  
        for i in range(len(intervals)):  
            if len(heap) == 0:  
                heapq.heappush(heap, intervals[i].end)  
                num += 1  
                continue  
            if heap[0] <= intervals[i].start:  
                heapq.heappop(heap)  
                heapq.heappush(heap, intervals[i].end)  
            else:  
                heapq.heappush(heap, intervals[i].end)  
                num +=1  
                  
        return num