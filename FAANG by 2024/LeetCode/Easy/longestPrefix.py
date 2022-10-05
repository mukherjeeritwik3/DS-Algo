#LeetCode - Easy

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pref = ""
        flag = False 
        i = 0
        while(flag!=True):
            try:
                temp = strs[0][i]
            except:
                return pref    
            for str in strs:
                try:
                   if temp != str[i]:
                        return pref

                except:
                    return pref
            i+=1
            pref+=temp

a = [""]
print(Solution().longestCommonPrefix(a))
