# Cosine similarity is a measure of similarity between two vectors of 
# an inner product space that measures the cosine of the angle between them.
 # The cosine of 0 is 1, and it is less than 1 for any other angle.
# Given two vectors A and B with the same size, calculate the cosine similarity.

# Return 2.0000 if cosine similarity is invalid (for example A = [0] and B = [0]).


 # example: Given A = [1, 2, 3], B = [2, 3 ,4].Return 0.9926.
 # Given A = [0], B = [0],Return 2.0000

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        # write your code here
        if not A or not B:
        	return 2.0
        if self.compute(A,A)==0 or self.compute(B,B)==0:
        	return 2.0
        else:
        	return 1.0*(self.compute(A,B))/((self.compute(A,A)*self.compute(B,B))**(.5))
    def compute(self,A,B):
		return sum([i*j for i,j in zip(A,B)])

