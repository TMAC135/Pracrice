

/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether 
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
  
    //1:do we have the case where the n is overflow or negative -- return 0
   //2: do we garantee that there must be a bad version? if not, if there is no
  //bad version, what value should we return
  //
  
    public int findFirstBadVersion(int n) 
    {
      if(n <= 0 || n >= Integer.MAX_VALUE) return 0;
      if(SVNRepo.isBadVersion(1)) return 1;
      if(!SVNRepo.isBadVersion(n)) return 0;
      
      //binary search,every time we garautee that 
      //SVNRepo.isBadVersion(start) == false and SVNRepo.isBadVersion(end)==true
      int start = 1;
      int end = n;
      int mid;
      while(start < end - 1)
      {
        mid = (start + end)/2;
        if(!SVNRepo.isBadVersion(mid)) start = mid;
        else end = mid;
      }
      return end;
    }
}