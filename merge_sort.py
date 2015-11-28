# coding=utf-8

"""
do the merge sort for the list:
still use the extra sapce when merge the two sorted list, 
how to implement merge use only O(1) space

"""


class Sort(object):
	"""docstring for Sort"""
	def mergesort(self,array):
		if not array:
			return []
		if len(array) == 1:
			return array
		mid = (len(array)-1)/2 
		array[:mid+1] = self.mergesort(array[:mid+1])
		array[mid+1:] = self.mergesort(array[mid+1:])
		return self.merge(array,mid)

	def merge(self,array,mid):
		length = len(array)
		left = 0
		right = mid + 1
		res = []
		while left <= mid and right < length:
			if array[left] < array[right]:
				res.append(array[left])
				left += 1
			else:
				res.append(array[right])
				right += 1
		res = res + array[left:mid+1] if left <= mid else res + array[right:]
		return res


if __name__ == '__main__':
	print Sort().mergesort([2,34,23,11,8,0,54,0,74,33])
	print Sort().mergesort([])



