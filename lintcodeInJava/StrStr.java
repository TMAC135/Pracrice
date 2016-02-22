

class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    public int strStr(String source, String target) 
    {
        // if(target == null || target.length() == 0) return true;
        // if(source == null || source.length() < target.length()) return false;
        if(target == null || source == null) return -1;

        for(int index=0; index <= source.length() - target.length(); index++)
        {
            if(helper(source,target,index)) return index;
        }
        return -1;
    }


    public static boolean helper(String source,String target, int index)
    {
        for(int i=0; i <  target.length(); i++)
        {
            if( !(source.charAt(index+i) == target.charAt(i)) ) return false;
        }
        return true
    }
}