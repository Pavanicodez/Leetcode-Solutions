# Leetcode problem 414: Third Maximum Number
from cmath import inf
class Solution():
    # Three variables
    def thirdMax(self,nums):
        first,second,third=float(-inf),float(-inf),float(-inf) # initializing 3 variables with negative infinity
        for i in nums:
            if i==first or i==second or i==third: # Checking duplicates
                continue
            if i>first: # if the current value is greater than first
                third=second # shifting current second to third largest 
                second=first # shifting current first to second largest
                first=i # shifting i value to first largest value
            elif i>second:
                third=second
                second=i
            elif i>third:
                third=i 
        if third==float(-inf):
            return first
        else:
            return third
        
    # Sorting method
    def thirdMax_sort(self,nums):
        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        if n<3:
            return max(nums)
        else:
            return nums[n-3]  
s=Solution()
arr=[0,3,3,0,2,2,0,4]
print(s.thirdMax(arr))
print(s.thirdMax_sort(arr))