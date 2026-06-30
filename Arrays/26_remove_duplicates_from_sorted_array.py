# Leetcode problem 26: Remove Duplicates from Sorted array
class Solution():
    #Fast and Slow pointers
    def removeDuplicates(self,nums):
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow]!=nums[fast]:#Check if both the elements are different
                slow+=1 # Changing the index of slow pointer
                nums[slow]=nums[fast]# Changing the first duplicate value with next unique value
        return slow+1
arr=[1,1,2,2,3]
sol=Solution()
k=sol.removeDuplicates(arr)
print(arr[0:k])