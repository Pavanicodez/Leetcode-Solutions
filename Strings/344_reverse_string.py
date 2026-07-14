# Leetcode problem 344: Reverse String
class Solution():
    def reverseString(self,s):
        i=0 # starting position
        j=len(s)-1 # last position
        while i<=j:
            s[i],s[j]=s[j],s[i] # swap first and last values
            i+=1
            j-=1
        return s 
# Test case
s=Solution()
arr=[1,0,5,6]
print(s.reverseString(arr))