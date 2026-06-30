# Leetcode problem 27: Remove Element
class Solution:
    # Two pointers
    def removeElement(self,nums,val):
        k=0 # index where the next non-target element should be placed
        # this helps to form the final array, removing the duplicates of target value
        for i in range(len(nums)):
            if nums[i]!=val: # Check if iterating value is not equal to given val
                nums[k]=nums[i] # Change the existing duplicate with current value 
                k+=1
        return k
# Test case
arr=[0,1,2,2,3,0,4,2]
n=Solution()
k=n.removeElement(arr,2)
print(k)
print(arr[0:k])