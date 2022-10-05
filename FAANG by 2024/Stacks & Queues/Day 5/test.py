class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1:
            return False
        stack = []
        lst = ['(' , '{' , '[']
        m = 0
        hashtb = {')':'(' , '}':'{' , ']':'['}
        for i in range(len(s)):
            if s[i] in lst:
                stack.append(s[i])
                continue
            if s[i] in [')','}',']']:
                if stack==[]:
                    return False
                if stack[-1]==hashtb[s[i]]:
                    
                    stack.pop()
                    m+=1
            
        return False if m==0 or stack !=[] else True        
s = Solution()
d="(])"
print(s.isValid(d))