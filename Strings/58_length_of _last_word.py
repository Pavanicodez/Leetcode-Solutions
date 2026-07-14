# Leetcode problem 58: Length Of Last Word
class Solution():
    def lengthOfLastWord(self,s):
        i=len(s)-1
        count=0
        while i>=0 and s[i]==" ": # to find last valid position 
            i-=1
        while i>=0 and s[i]!=" ": # to count length of lasst word
            count+=1
            i-=1
        return count
# Test Case
s=Solution()
print(s.lengthOfLastWord("Hello World  "))