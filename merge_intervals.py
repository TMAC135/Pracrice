# Given a collection of intervals, merge all overlapping intervals.

# example:
# [[2,3],[2,6],[8,10]] => [[1,6],[8,10]]

# challenge: 
# O(n log n) time and O(1) extra space.



"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution(object):
    # @param intervals, a list of Interval
    # @return a list of Interval

    """
    It takes me almost much time to debug it on the OJ.
    The main though behind this is first to sort the 
    original intervals by the start, then we are keeping
    scaning in the intervals.
    Notice 
    ss: is to track the start value of the final interval
    value: end value for the final interval
    down :is the index we want to compare with  value
    """

    def merge(self, intervals):
        # write your code here

        if not intervals:
        	return []
        res=[]
        intervals.sort(key=lambda x:x.start)
        return intervals[0]
        ss=0
        down=0
        value=intervals[ss].end
        while down < len(intervals):
        	# append the inteval since we are sure it has no 
        	# overlap with previous value
        	if value < intervals[down].start:
        		res.append([intervals[ss].start,value])
        		ss=down # be care of the update, cost me time to debug
        		value=intervals[down].end
        	# update the value
        	else:
        	    if value <= intervals[down].end:
        		    value=intervals[down].end
        	down+=1
        # jump out the loop, then we need to append last inteval
        res.append([intervals[ss].start,value])
        # i get the wrong return value, although it pass the OJ,
        # the problem want to return the list of intervals which 
        # is list of object.
        return res



# the same idea as me, but get the right output
class Solution2(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        lenInter = len(intervals)
        if lenInter == 0:
            return intervals

        #Another sorting method: intervals = sorted(intervals, key=lambda inter: inter.start)
        intervals.sort(key=lambda inter: inter.start)

        rsIntervals = []

        curInterval = intervals[0]
        for i in range(1, lenInter):
            if intervals[i].start > curInterval.end:
                rsIntervals.append(curInterval)
                curInterval = intervals[i]
            else:
                curInterval.end = max(curInterval.end, intervals[i].end)

        rsIntervals.append(curInterval)

        return rsIntervals



if __name__=='__main__':
	a,b,c=Interval(1,4),Interval(0,10),Interval(3,5)
	test=[a,b,c]
	A=Solution()
	print A.merge(test)







