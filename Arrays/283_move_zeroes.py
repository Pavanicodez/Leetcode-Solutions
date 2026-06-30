# Leetcode problem 283: Move Zeroes
class Solution():
    # Two pointers
    def moveZeroes(self,nums):
        j=0 # index used to indicate zeroes
        for i in range(len(nums)):
            if nums[i]!=0: # Check if the current value is non-zero
                nums[i],nums[j]=nums[j],nums[i] # Then swap it with the zero value using index j
                j+=1
        return nums
# Test case
s=Solution()
arr=[0]
print(s.moveZeroes(arr))