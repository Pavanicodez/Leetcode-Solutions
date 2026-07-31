# Leetcode problem 03: Longest Substring without Repeating Characters
class Solution:
    # Sliding window approach
    def lengthOfLongestSubstring(self,s):
        l=0 # left index
        char_set=set()
        max_len=0
        for r in range(len(s)): # right index
            while s[r] in char_set:
                char_set.remove(s[l]) 
                l+=1 # shrinking left, if any duplicate is found until it is removed from the window
            char_set.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len
# Test Case
s=Solution()
print(s.lengthOfLongestSubstring("pwwkew"))