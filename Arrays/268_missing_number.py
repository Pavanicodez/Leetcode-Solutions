# Leetcode problem 268: Missing Number
class Solution():
    def missingNumber(self,nums):
        n=len(nums)
        expected_sum=n*(n+1)//2 # total sum of the numbers from 0 to n
        actual_sum=sum(nums) # actual sum of values in nums array
        return expected_sum-actual_sum # missing value
# Test Case
s=Solution()
print(s.missingNumber([0,1,2,4,5,6,7,8,9])) 