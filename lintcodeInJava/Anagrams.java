
/*
Given an array of strings, return all groups of strings that are anagrams

note:All input will be in lower cases
*/

import java.util.*;

public class Anagrams{

	public static ArrayList<String> anagrams(String []_str){
		// bound condition
		if(_str == null){
			return null;
		}
		// hashmap 
		HashMap<Integer,ArrayList<String>> _myMap = new HashMap<>();
		ArrayList<String> _result = new ArrayList<>();

		//Map the string to hashmap 
		for(String s:_str){
			int[] _array = new int[26];// initilization for array is all zero
			// convert the string to a int array, in order to compute the hashcode for each string
			for(int i=0; i<s.length();i++){
				_array[s.charAt(i)-'a']++;
			}
			int _hashcode = getHashCode(_array);

			if(!_myMap.containsKey(_hashcode)){
				_myMap.put(_hashcode,new ArrayList<String>());
			}else{
				_myMap.get(_hashcode).add(s);
			}
		}

		//extract the case where there are anagrams
		for(ArrayList<String> arrayList:_myMap.values()){
			if(arrayList.size() >= 2) _result.addAll(arrayList); 
		}
		return _result;
		
	}

	/*calculate the hash code for char array for each string
	*/
	public static int getHashCode(int[] _c){
		int _hash = 0;
		int _a = 378551;
		int _b = 63689;
		for(int num:_c){
			_hash = _hash*_a+num;
			_a = _a*_b;
		}
		return _hash;
	}


	/*Test method
	*/
	public static void main(String[] args) {
	String[] strs = new String[4];
	strs[0]="abcd";
	strs[1]="abetg";
	strs[2]="cdab";
	strs[3]="ac";
	ArrayList<String> s1 = anagrams(strs);
	for(String s:s1){
		System.out.println(s);
	}

	}
}