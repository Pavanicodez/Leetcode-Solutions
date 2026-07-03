# Leetcode problem 169: Majority Element
class Solution():
    def majorityElement(self,nums):
        hashmap={} # empty hashmap
        n=len(nums)
        for i in nums:
            # handling single element case
            if n==1: # returning the value as major if there exists only one element
                return i
            if i not in hashmap:
                    hashmap[i]=1
            else:
                hashmap[i]+=1 
                if hashmap[i]>n//2: # if the count is more than (n/2)
                    return i
# Test Case
s=Solution()
print(s.majorityElement([2,2,1,1,2,2]))