class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        last = '1'
        for ii in xrange(2, n+1):
            current = ''
            occur = 1
            for jj, c in enumerate(last[1:]):
                if c == last[jj-1]:
                    occur += 1
                else:
                    current+= str(occur) + last[jj:]
                    occur = 1
            last=current
        return current
