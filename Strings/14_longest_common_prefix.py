# Leetcode problem 14: Longest Common Prefix
class Solution():
    def longestCommonPrefix(self,strs):
        prefix="" # empty prefix string 
        for i in range(len(strs[0])):
            ch=strs[0][i] # each cahracter of first string
            for j in range(1,len(strs)): 
                if i==len(strs[j]) or ch!=strs[j][i]: # Checking the same position in other strings
                    # if the index of current character is equal to the length of comparing string,
                    # stop the loop since that index doesn't exist in comparing string 
                    return prefix 
            prefix+=ch
        return prefix 
#Test Case
s=Solution()
list=["flower","flow","flight"]
print(s.longestCommonPrefix(list))