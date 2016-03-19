
/*
Implement a trie with insert, search, and startsWith methods.

eg:
insert("lintcode")
search("code") // return false
startsWith("lint") // return true
startsWith("linterror") // return false
insert("linterror")
search("lintcode) // return true
startsWith("linterror") // return true
*/


/**
 * Your Trie object will be instantiated and called as such:
 * Trie trie = new Trie();
 * trie.insert("lintcode");
 * trie.search("lint"); will return false
 * trie.startsWith("lint"); will return true
 */
class TrieNode {
    public char value;
    public TrieNode[] next;
    public boolean isEnd;
    // Initialize your data structure here.
    public TrieNode() {
        next = new TrieNode[26];
        //first set null value to all array elements when we create the node
        for(int i=0;i<26;i++)
        {
            next[i] = null;
            isEnd = false;
        }
    }
    
}

public class Solution {
    private TrieNode root;

    public Solution() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        if(word == null || word.length() == 0) return;
        
        word.toLowerCase();//lower case 
        int index;
        TrieNode cur = root;
        for(char c:word.toCharArray())
        {
            index = c - 'a';
            if(index < 0 || index >= 26) continue;//invalid char,we just ignore it 
            
            if(cur.next[index] == null)
            {
            //set the value of the current char node
            TrieNode tmp = new TrieNode();
            tmp.value = c;
            cur.next[index] = tmp;
            cur = tmp;
            }else
            {
                cur = cur.next[index];
            }
        }
        cur.isEnd = true;//once we hit the end of a word, we set the attribute of the current node(isEnd) true 
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        if(word == null || word.length() == 0) return true;
        word.toLowerCase();
        TrieNode cur = root;
        int index;
        for(char c:word.toCharArray())
        {
            index = c - 'a';
            if(index < 0 || index >=26) continue;
            
            if(cur.next[index] == null) return false;
            else cur = cur.next[index];
        }
        return true?cur.isEnd == true:false;
        
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        if(prefix == null || prefix.length() == 0) return true;
        prefix.toLowerCase();
        TrieNode cur = root;
        int index;
        for(char c:prefix.toCharArray())
        {
            index = c - 'a';
            if(index < 0 || index >=26) continue;
            
            if(cur.next[index] == null) return false;
            else cur = cur.next[index];
        }
        return true;
    }
}