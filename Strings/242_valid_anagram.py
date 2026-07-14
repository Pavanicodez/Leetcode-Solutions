# Leetcode problem 242: Valid Anagram
class Solution():
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        freq={}
        for i in s: # storing all keys and values of characters in the string s
            freq[i]=freq.get(i,0)+1
        for i in t: # Checking the values in string t
            if i not in freq:
                return False
            freq[i]-=1
            if freq[i]==0: # deleting empty key
                del freq[i]
        if freq=={}:
            return True 
        else:
            return False 
# Test Case
s=Solution()
print(s.isAnagram("anagram","nagaram"))