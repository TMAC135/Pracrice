public class Solution 
{
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
  /*
  what is the case ArrayList is empy or have only one element?
  */
    public ArrayList<Long> productExcludeItself(ArrayList<Integer> A) 
    {
      ArrayList<Long> res = new ArrayList<>();
      //bound case
      if(A.isEmpty() || A == null) return res;
      if(A.size() == 1){
          long tmp = 1;
        res.add(tmp);
        return res;
      }
      
      for(int i=0;i < A.size();i++)
      {
        long product = 1;
        for(int j=0; j<A.size();j++)
        {
          if(i == j) continue;
          else product *= A.get(j);
        }
        //write the result into the result arraylist
        res.add(product);
      }
      return res;
    }
}