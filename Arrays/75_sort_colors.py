# Leetcode problem 75: Sort Colors
class Solution():
    def sortColors(self,nums):
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1
        return nums
# Test Case
s=Solution()
arr=[2,2,0,1,0]
print(s.sortColors(arr))