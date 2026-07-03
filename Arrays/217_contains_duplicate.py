# Leetcode problem 217: Contains Duplicate
class Solution():
    # Hashmap method
    def containsDuplicate(self,nums):
        hashmap={} # empty hashmap
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1 # count every element
            else:
                return True # if there's a duplicate
        return False
    # Set method
    def containsDuplicateSet(self,nums):
        return len(nums)!=len(set(nums)) # since set contains unique values, length varies
# Test Case
s=Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicateSet([1,2,3,1]))