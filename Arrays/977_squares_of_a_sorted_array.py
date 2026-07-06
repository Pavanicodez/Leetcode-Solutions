# Leetcode problem 977: Squares of a sorted array
class Solution():
    def sortedSquares(self,nums):
        i=0
        j=len(nums)-1
        result=[0]*len(nums) # creating an empty array of size same as nums
        k=len(nums)-1 # used to maintain the index of result array
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                result[k]=pow(nums[j],2)
                k-=1
                j-=1
            else:
                result[k]=pow(nums[i],2)
                k-=1
                i+=1
        return result
# Test Case
s=Solution()
arr=[-10,-7,2,3,11]
print(s.sortedSquares(arr))