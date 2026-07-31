# Leetcode problem 151: Reverse words in a string
class Solution():
    def reverseWords(self,s):
        words=s.split()
        words.reverse()
        return " ".join(words)
# Test Case
s=Solution()
print(s.reverseWords("the sky is blue"))