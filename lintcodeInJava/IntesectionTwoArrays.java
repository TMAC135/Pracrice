

// intersection of two arrays
/*
how to deal with the repeated element
can we use Array sort in the package
*/

public class Solution
{
	//we the intersection array may contain duplicated elements

	//1: brute force - O(nm)
		public static ArrayList<Integer> intersection1(int[] array1, int[] array2)
		{
			ArrayList<Integer> res = new ArrayList<Integer>();
			if(array1 == null || array2 == null || array1.length == 0 || array2.length == 0) return res;
			for(int i=0;i<array1.length;i++)
			{
				//if(array1[i] == prev) continue;
				for(int j=0;j<array2.length;j++)
				{
					if(array2[j] == array1[i])
					{
						res.add(array1[i]);
						break;
					}
				}
//				prev = array1[i];
			}
			return res;
		}

		//2: binary search - min(O(nlogm),O(mlogn))
		public static ArrayList<Integer> intersection2(int[] array1, int[] array2)
		{
			ArrayList<Integer> res = new ArrayList<Integer>();
			if(array1 == null || array2 == null || array1.length == 0 || array2.length == 0) return res;
			// we find the maximum length and sort it
			if(array1.length <= array2.length)
			{
				int[] arraySort = new int[array2.length];
				System.arraycopy(array2,0,arraySort,0,array2.length);
				Arrays.sort(arraySort);

				int[] arrayWalk = new int[array1.length];
				arrayWalk = array1;
			}else
			{
				int[] arraySort = new int[array1.length];
				System.arraycopy(array1,0,arraySort,0,array1.length);
				Arrays.sort(arraySort);

				int[] arrayWalk = new int[array2.length];
				arrayWalk = array2;
			}

			for(int i=0;i< arrayWalk.length;i++)
			{
				if(binarySearch(arraySort,arrayWalk[i])) res.add(arrayWalk[i]);
			}
			return res;
		}

		public static boolean binarySearch(int[] array, int target)
		{
			if(target < array[0] || target >array[array.length]) return false;
			if(target == array[0] || target == array[array.length]) return true;
			int start = 0;
			int end = array.length;
			int mid = 0;
			//end case, where start = end - 1
			while(start < end - 1)
			{
				mid = (start + end) / 2;
				if(array[mid] > target) end = mid;
				else if(array[mid] < target) start = mid;
				else return true;
			}
			return false;
		}

		//3:Hash Map, O(n + m) complexity, 好像没解决重复的问题
		public static ArrayList<Integer> intersection3(int[] array1, int[] array2)
		{
			ArrayList<Integer> res = new ArrayList<Integer>();
			if(array1 == null || array2 == null || array1.length == 0 || array2.length == 0) return res;

			HashMap<Integer, Integer> myMap = new HashMap<Integer, Integer>();
			for(int i=0;i<array1.length;i++)
			{
				if(!myMap.containsKey(array1[i])) myMap.put(array1[i],1);
				else
				{
					int tmp = myMap.get(array1[i]);
					myMap.replace(array1[i], tmp++);
				}
			}
			for(int j=0;j<array2.length;j++)
			{
				if(!myMap.containsKey(array2[j])) continue;
				else
				{
					res.add(array2[j]);
					if(myMap.get(array2[j]) > 1)
					{
						int tmp = myMap.get(array2[j]);
						myMap.replace(array2[j],tmp--);
					}
					else myMap.remove(array2[j]);
				}
			}
			return res;
		}

www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=147297&fromuid=109727

}