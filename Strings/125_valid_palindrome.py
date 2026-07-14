# Leetcode problem 125: Valid Palindrome
class Solution():
    def isPalindrome(self,s):
        left=0
        right=len(s)-1
        while left<=right:
            if not s[left].isalnum():# Skip non-alphanumeric values
                left+=1
                continue
            if not s[right].isalnum():# Skip non-alphanumeric values
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
# Test Case
s=Solution()
print(s.isPalindrome("Race a Car"))