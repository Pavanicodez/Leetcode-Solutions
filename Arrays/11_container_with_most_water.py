# Leetcode problem 11: Container with most water
class Solution():
    def maxArea(self,nums):
        l=0
        r=len(nums)-1
        max_area=0
        while l<r:
            max_area=max(min(nums[l],nums[r])*(r-l),max_area)
            if nums[l]<nums[r]:
                l+=1 
            else:
                r-=1 
        return max_area 
# Test Case
s=Solution()
arr=[1,8,6,2,5,4,8,3,7]
print(s.maxArea(arr))