# Leetcode problem 53: Maximum subarray
class Solution():
    # Kadane's Algorithm
    def maxSubArray(self,nums):
        cs=nums[0] # current sum
        ms=nums[0] # maximum sum 
        for n in nums[1::]:
            cs=max(cs+n,n) # continuing the subarray if current sum is greater than the present value
            ms=max(ms,cs) # updating the maximum sum
        return ms 
# Test case
s=Solution()
arr=[5,4,-1,7,8]
print(s.maxSubArray(arr))