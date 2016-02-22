

/*

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
*/

/*
Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
*/


/*
这题我没有做出来，看了几个别人的答案，可以用dfs(递归)和bfs来做
参考：http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/

但是基本思路是我们尝试一个字符一个字符的删除，然后再判断是否是合理的，因此我们要有判断字符串是否合法的
函数，即isValid(String s),或者统计整个字符串中左右括号失匹配的个数findMisMatch(String s).

还有一个问题是因为题目要求是必须是移除最少的括号得到的结果，这时候如果我们如果用dfs,我们需要比较如果失匹配的
少于前一个，则继续搜索，否则停止搜索。如果用bfs的话，我们就需要用一个queue和一个flag, 其中flag代表我们是否停止
向queue中加入可能的元素。

两种方法都需要枚举，即取出每个字符，再进行下次判断，还有更巧妙的算法还没看懂。
*/

/*
python 代码：
1:dfs:
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s):
            mi = calc(s)
            if mi == 0:
                return [s]
            ans = []
            for x in range(len(s)):
                if s[x] in ('(', ')'):
                    ns = s[:x] + s[x+1:]
                    if ns not in visited and calc(ns) < mi:
                        visited.add(ns)
                        ans.extend(dfs(ns))
            return ans    
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])    
        return dfs(s) 


2: bfs:
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            a = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                if a < 0:
                    return False
            return a == 0

        visited = set([s])
        ans = []
        queue = collections.deque([s])
        done = False
        while queue:
            t = queue.popleft()
            if isValid(t):
                done = True
                ans.append(t)
            if done:
                continue
            for x in range(len(t)):
                if t[x] not in ('(', ')'):
                    continue
                ns = t[:x] + t[x + 1:]
                if ns not in visited:
                    visited.add(ns)
                    queue.append(ns)

        return ans
*/