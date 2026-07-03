# Leetcode problem 88: Merge Sorted Array
class Solution():
    def merge(self,nums1,m,nums2,n):
        i=m-1 # last valid index in nums1
        j=n-1 # last inex in nums2
        k=m+n-1 # last empty index in nums1, used to place the value
        while i>=0 and j>=0:
            if nums2[j]>nums1[i]: # check which value is greater
                nums1[k]=nums2[j] # greater value is place at the end
                k-=1 # and the k index is moved left
                j-=1 # and greater value's index is also moved to left
            else:
                nums1[k]=nums1[i]
                k-=1
                i-=1
        while j>=0: # copying remaining values of nums2 
            nums1[k]=nums2[j]
            k-=1
            j-=1
        return nums1 
# Test Case
s=Solution()
print(s.merge([2,3,0,0],2,[2,3],2))