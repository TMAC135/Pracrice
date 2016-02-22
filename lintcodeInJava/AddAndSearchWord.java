

/*
Design a data structure that supports the following two operations: addWord(word) and search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or ..

A . means it can represent any one letter.

Example
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
*/

/*
classification: 
1: so i am wondering is the word you are add or search only consits of lower case letter?
2: Can I use hashset structure to store the words?
3:how to handle the case which word is null or empty?
*/
public class WordDictionary 
{
    private HashSet<String> set = new HashSet<>();
    // Adds a word into the data structure.
    public void addWord(String word) 
    {
      if(word == null) return;
      if(!set.contains(word)) set.add(word);
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) 
    {
      if(word == null) return false;
      Iterator<String> iter = set.iterator();
      
      while(iter.hasNext())
      {
        String tmp = iter.next();
        if(helper(tmp,word)) return true;
      }
      return false;
    }
  
    //helper function to help checking whether two words match
    private static boolean helper(String tmp,String word)
    {
      //boundary case
      if(tmp.length() == 0 && word.length() == 0) return true;
      if(word.length() != tmp.length()) return false;
      
      //pass through word and tmp at the same time
      for(int i=0;i<tmp.length();i++)
      {
        if(word.charAt(i) == '.' || word.charAt(i) == tmp.charAt(i)) continue;
        else return false;
      }
      return true;
    }
}
