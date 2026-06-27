# Leetcode problem 1: Two Sum
class Solution:
    def twoSum(self,nums,target):
        hashmap={} # Creating empty Hashmap
        for i in range(len(nums)):
            c=target-nums[i] # Find the complement needed to reach the target
            if c in hashmap: # Check if the complement already exists in  hashmap
                return [hashmap[c],i] # Return the indices of two numbers
            hashmap[nums[i]]=i # Store the current number and its index
# Test case
nums=Solution()
print(nums.twoSum([2,7,11,19],9))