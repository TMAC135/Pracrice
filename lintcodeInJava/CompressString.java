//coding=utf-8

/** Implement a method to compress string with the original character and
*repeated count. For example, "aabbcdddd" => "a2b2c1d4"
*If the compressed string woundn't become smaller, then return the original string
*
*/

// Three important things :
// 1: Difference between int and string, like 10 and "10", if we count the 
// number of the reapeaded character, we need to convert it to string.

// 2: If there is no repeaded character in the original string, like "abcdefg", then 
// if we still compress it -> "a1b1c1d1e1f1g1", obviously we have larger length, 
// but according to the problem, we need to return the original one. Thus we can't 
// just compress it directly without eliminating the case where no repeaded case.CompressedSize()
// is the method to calculate the size of string after compression.

// 3: Differences between String and StringBuffer: Concatenation will cause extra space 
// complexty for String. Like "a" + "aa" + "aaa" ... => O(n^2) space. So Suggest using StringBuffer.



public class CompressString
{
	public static void main(String[] args) 
	{
		String[] test = new String[]{"abcd","aaswec","aaaaaaaaaaaaaabcc","abbbbbbbbbbbbbbbbb"};
		for(String s:test)
		{
			System.out.println(compressString(s));
		}
		
	}

	/** Using String Buffer to avoid cost for concatanation of the string
	*/
	public static String compressString(String str)
	{
		int size = compressedSize(str);
		if(size >= str.length())
		{
			return str;
		}

		StringBuffer stringBuffer = new StringBuffer();
		char last = str.charAt(0);
		int count = 0;
		for(int i=0;i<str.length();i++)
		{
			if(str.charAt(i) == last)
			{
				count++;
			}else
			{
				stringBuffer.append(last);
				//count is the int type, we need to transfer
				stringBuffer.append(String.valueOf(count));
				last = str.charAt(i);
				count = 1;
			}
		}
		//append the last bit bit and count
		stringBuffer.append(last);
		stringBuffer.append(String.valueOf(count));
		return stringBuffer.toString();

	}

	/** This function is used to calculate the size of string after compression 
	*/
	public static int compressedSize(String str)
	{
		if(str == null || str.isEmpty())
		{
			return 0;
		}
		char last = str.charAt(0);
		int count = 0;
		int size = 0;
		for(int i=0;i<str.length();i++)
		{
			if(str.charAt(i) == last)
			{
				count ++ ;
			}else
			{
				// a little trick to compute the length of a int type value
				size += 1 + String.valueOf(count).length();
				last = str.charAt(i);
				count = 1;
			}
		}
		size += 1 + String.valueOf(count).length();
		return size;
	}

	
	/*We can also use the char array to solve this problem since we already know
	*the actual length of the compressed string. 
	*/


}