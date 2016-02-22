
/*
Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
*/


class Solution 
{
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) 
    {
      //boundary cases
      if(n == 0) return;
      
      //two pointers for the two array from the end of the arrays
      int indexB = n - 1;
      int indexA = m - 1;
      
      int merge = n + m -1;
      while(merge >= 0)
      {
        //determine whether the index of A and B are valid
        if(indexA < 0)
        {
          while(indexB >=0)
          {
            A[merge--] = B[indexB--];
          }
          return;            
        }
        if(indexB < 0)
        {
          return;
        }
        
        if(A[indexA] >= B[indexB])
        {
          A[merge--] = A[indexA--];
        //   indexA--;
        }else
        {
          A[merge--] = B[indexB--];
        //   indexB--;
        }
        // merge--;        
      }
    }
}