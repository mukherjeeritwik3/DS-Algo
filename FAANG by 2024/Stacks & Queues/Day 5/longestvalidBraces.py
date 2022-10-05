#LeetCode - Hard

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        stack = []

        for ch in s:
            if ch == "(":
                if  stack !=[] and stack[-1]=="(":
                    l=0
                stack.append(ch)
            elif ch ==")":
                if stack!=[] and stack[-1]=="(":
                    stack.pop()
                    l+=2     
        return l
s = Solution()
str = "()(()))()()"
print(s.longestValidParentheses(str))        