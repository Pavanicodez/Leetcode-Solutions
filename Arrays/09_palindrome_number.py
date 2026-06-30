# Leetcode problem 9: Palindrome Number
# String reverse method
class Solution():
    def isPalindrome(self,x):
        x=str(x) 
        if x==x[::-1]:
            return True
        return False
# Without converting int to string
    def isPalindromeInt(self,x):
        r=0 # Reverse number
        d=0 # Digit 
        xsave=x # Storing the original int 
        while x>0:
            d=x%10 # Separating the digit
            r=r*10+d # Adding the digit 
            x//=10 # Removing the last digit
        if r==xsave:
            return True
        else:
            return False
# Test Case
s=Solution()
print(s.isPalindrome(0))
print(s.isPalindromeInt(0))