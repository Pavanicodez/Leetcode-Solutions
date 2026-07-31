# Leetcode problem 28: Find the Index of the First Occurence in a String 
class Solution():
    def strStr(self,haystack,needle):
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1
#Test Case
s=Solution()
print(s.strStr("sadbutsad","sad"))