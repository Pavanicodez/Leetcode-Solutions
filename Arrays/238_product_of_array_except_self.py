# Leetcode problem 238: Product of array except itself
class Solution():
    def productExceptSelf(self,nums):
        ans=[1]*len(nums) # Initializing output array
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1] # prefix product array
        rightproduct=1 # maintaining product of right side elements of current value
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=rightproduct
            rightproduct*=nums[i]
        return ans
#Test Case
s=Solution()
arr=[1,2,3,4]
print(s.productExceptSelf(arr))