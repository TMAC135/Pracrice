#Given n points on a 2D plane, find the maximum 
# 	number of points that lie on the same straight line.

#my answer, the first idea came from me is to calculte the slope of every 
#	two points,  which after 2 hours, I figure out it is definitely wrong,
#	since the key point here is to find the points in the same line, so we need to check 
#	this condition


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        if not points:
        	return 0
        if len(points)==1:
            return 1
        hash = dict(inf=[])
        for i in xrange(len(points)-1):
        	point = points[i]
        	rep = 1
        	for j in xrange(i+1,len(points)):
        		if points[j].x == point.x and points[j].y == point.y:
        		   	rep += 1
        			continue
        		if points[j].x != point.x:
        			k = (points[j].y-point.y)/float((points[j].x-point.x))
        			if hash.has_key(str(k)) == 0:  # try if hash.has_key(str(k))
	        			hash[str(k)] =[]
	        			# if point in hash[str(k)]: # check whether point is in the hash[str(k)]
	        			# 	hash[str(k)].append(points[j])
	        			# else:
	        			# tep=[point,points[j]]
	        			# hash[str(k)].extend(tep)
	        		# else:
	        			# if point in hash[str(k)]:
	        			# 	if poin[j] in hash[str(k)]:
	        			# 		continue
		        		# 	else:
		        		# 		hash[str(k)].append(points[j])
		        		# else:
		        		# 	hash[str(k)].append(points[j])
		        	tep=[point,points[j]]
		        	hash[str(k)].extend(tep)
        		else:
        			tep=[point,points[j]]
        			hash['inf'].extend(tep)
        			# if point in hash['inf']:
        			# 	hash['inf'].append(points[j])
        			# else:
	        		# 	tep=[point,points[j]]
	        		# 	hash[str(k)].extend(tep)
	        	if rep == len(points):
	        	    return rep

        key = hash.keys()
        # return hash
        max=0
        for item in key:
        	if len(list(set(hash[item])))>max:
        		max=len(list(set(hash[item])))
        return [max,key,hash]

##Code from others:
# class Solution:
#     # @param points, a list of Points
#     # @return an integer
#     def maxPoints(self, points):
#         length = len(points)
#         if length < 3: return length
#         res = -1
#         for i in range(length):
#             slope = {'inf': 0}
#             samePointsNum = 1
#             for j in range(length):
#                 if i == j:
#                     continue
#                 elif points[i].x == points[j].x and points[i].y != points[j].y:
#                     slope['inf'] += 1
#                 elif points[i].x != points[j].x:
#                     k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
#                     if k not in slope:
#                         slope[k] = 1
#                     else:
#                         slope[k] += 1
#                 else:
#                     samePointsNum += 1
#             res = max(res, max(slope.values()) + samePointsNum)
#         return res




