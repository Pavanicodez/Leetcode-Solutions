# Leetcode problem 344: First Unique Character in a String
class Solution():
    def firstUniqueChar(self,s):
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
# Test case
s=Solution()
print(s.firstUniqueChar("loveleetcode"))