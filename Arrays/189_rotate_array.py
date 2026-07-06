# Leetcode problem 189: Rotate Array
class Solution():
    def rotate(self,nums,k):
        n=len(nums)
        k%=n # removes excess rotations
        nums.reverse() # reverse entire array
        nums[:k]=reversed(nums[:k]) # reverse first k items
        nums[k:]=reversed(nums[k:]) # reverse items after kth position
        return nums
s=Solution()
print(s.rotate([1,2,3,4,5,6,7],3))