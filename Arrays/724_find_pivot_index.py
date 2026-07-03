# Leetcode problem 724: Find Pivot Index
class Solution():
    def pivotIndex(self,nums):
        left_sum=0 
        total_sum=sum(nums) # calculating the total sum of the array
        for i in range(len(nums)):
            right_sum=total_sum-left_sum-nums[i] # calculating the right sum
            if right_sum==left_sum: # checking the left and right sum  
                return i 
            left_sum+=nums[i]
        return -1
# Test case
s=Solution()
arr=[1,7,3,6,5,6]
print(s.pivotIndex(arr))