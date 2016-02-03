//coding=utf-8


public class ClimbingStairs{
	// test method
	public static void main(String[] args) {
		System.out.println(climb(10));
		System.out.println(climb2(10));
	}

	// Use recursion way 
	public static int climb(int _n){
		if(_n <= 2){
			return _n;
		}
		return climb(_n-1)+climb(_n-2);
	}

	//Use Iteration: f(n) = f(n-1) + f(n-2)
	public static int climb2(int _n){
		if(_n <= 2){
			return _n;
		}
		int last=1;
		int lastlast=1;
		int result = 0;
		for(int i=2;i<=_n;i++){
			result = last + lastlast;
			lastlast = last;
			last = result;
		}
		return result;
	}

}