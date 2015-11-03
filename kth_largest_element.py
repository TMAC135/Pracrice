"""
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.
In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

Note
You can swap elements in the array

Challenge
O(n) time, O(1) extra memory.

"""



class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    """
    naive solution with sorting
   	the time complexity is O(nlog(n)) not optimized solution
    """
    def kthLargestElement(self, k, A):
        if not A:
            return 0
        A.sort()
        return A[-k]

     
    """
    use thought of the quick sort and partition the array according to the 
    pivot we choose. If we choose the pivot just from the left in the 
    array, the worst case is O(n^2) but the average time complexity is O(n).

    once we find the 
    """   
    def findKthLargest(self, nums, k):
    	if not A:
    		return 0
    return self.quickSelect(nums, 0, len(nums)-1, k)

	def quickSelect(self, nums, start, n, k): # quick select
	    pos = self.partition(nums, start, n)
	    if pos == k-1:
	        return nums[pos]
	    elif pos >= k:
	        return self.quickSelect(nums, start, pos - 1, k)
	    return self.quickSelect(nums, pos + 1, n, k)

	def partition(self, nums, left, right):
	    pivot = nums[right] # pick the last one as pivot
	    i = left
	    for j in xrange(left, right): # left to right -1
	        if nums[j] > pivot: # the larger elements are in left side
	            nums[j], nums[i] = nums[i], nums[j]
	            i += 1
	    nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
	    return i

	    """
	    to avoid the worst case of O(n^2) time, we can use the mean of the
	    first 3 or 5 elements in the array

	    """
    def kthLargestElement(self, k, A):
        if not A:
            return 0

        """
        use maximum heap, first constuct a maximum heap and it cost O(n), and 
        then excute k-1 times of extractMax() operations. Thus the total time complexity 
        is O(n+klogn)

        here is the code for c++ from others:
        """
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        heapSize_ = nums.size();
         
        createMaxHeap(nums);
        for (int i = 0; i < k - 1; ++i) {
            exactMax(nums);
        }
         
        return nums[0];
    }
     
private:
    int heapSize_;
     
    inline int leftChild(int parent) {
        return (parent << 1) + 1;
    }
     
    inline int rightChild(int parent) {
        return (parent << 1) + 2;
    }
     
    inline int parent(int child) {
        return (child - 1) >> 1;
    }
     
    void createMaxHeap(vector<int> &nums) {
        int indexForHeapify = parent(heapSize_ - 1);
        for (int i = indexForHeapify; i >= 0; --i) {
            maxHeapify(nums, i);
        }
    }
     
    // 从位置i处进行下滤，保持大顶堆的偏序性
    void maxHeapify(vector<int> &nums, int i) {
        int left = leftChild(i);
        int right = rightChild(i);
        int largest = i;
         
        if (left < heapSize_ && nums[left] > nums[largest]) {
            largest = left;
        }
         
        if (right < heapSize_ && nums[right] > nums[largest]) {
            largest = right;
        }
         
        if (largest != i) {
            swap(nums[largest], nums[i]);
            maxHeapify(nums, largest);
        }
    }
     
    void exactMax(vector<int> &nums) {
        swap(nums[0], nums[heapSize_ - 1]);
        --heapSize_;
        maxHeapify(nums, 0);
    }
};






