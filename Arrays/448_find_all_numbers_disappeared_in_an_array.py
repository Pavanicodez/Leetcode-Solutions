# Leetcode problem 448: Find all numbers disappeared in an Array
class Solution():
    def findDisappearedNumbers(self,nums):
        for num in nums:
            index=abs(num)-1
            if nums[index]>0:
                nums[index]=-nums[index] # marking the indices of visited numbers
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                result.append(i+1) # appending values of unmarked indices to result array
        return result
#Test Case
s=Solution()
print(s.findDisappearedNumbers([1,1]))