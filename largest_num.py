# coding=utf-8

"""
Given a list of non negative integers, arrange them such that they form the largest number

Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.

Note
The result may be very large, so you need to return a string instead of an integer.

"""

class Solution:
    # @param num, a list of integers
    # @return a string
    """
    没想出来，卡在了如何比较不相同长度，目的是要每次加入左边的书尽量大的数字，但是给出的
    数字并不是等长度的，因此如何将这些不同长度的数字来进行排序，是重点

    此题别人根据python中相同长度的 数字字符串 比较，若不相同，则互相粘在对方字符串里
    就变成了相同字符串。即下列方法中的 compare 函数. 利用字典来记录相同数字的个数，然后
    最后输出答案。

    另外注意sort,max...函数有key,cmp,reverse 参数可以设置。
    """

    def largestNumber(self, num):
        def compare(num1, num2):
            if len(num1) != len(num2):
                num1,num2 = num1 + num2,num2 + num1
            return [-1, 1][num1 > num2]


        d = {}
        for n in num:
            n = str(n)
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

        keys = d.keys()
        keys = sorted(keys, cmp=compare, reverse=True)

        result = ""
        for k in keys:
            result = result + str(k) * d[k]

        result = result.lstrip('0')
        if len(result) == 0:
            return "0"
        else:
            return result



if __name__ == '__main__':
	print Solution().largestNumber([20,20,20,20,20])

