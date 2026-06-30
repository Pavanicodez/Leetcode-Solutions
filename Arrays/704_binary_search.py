# Leetcode problem 704: Binary Search
class Solution():
    def search(self,nums,t):
        l=0 # Starting position
        r=len(nums)-1 # Ending position 
        while l<=r:
            m=l-((l-r)//2) # Calculating mid index
            if nums[m]<t: # if mid value is less than target
                l=m # move left pointer to mid index
            elif nums[m]>t: # if mid value is greater than target
                r=m # move right pointer to mid index
            else: # if mid==target
                return m 
        return -1
# Test Case
s=Solution()
arr=[-1,0,3,5,9,12]
print(s.search(arr,9))