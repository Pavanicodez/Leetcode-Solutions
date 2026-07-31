# Leetcode problem 383: Ransom Note
class Solution():
    def canConstruct(self,ransomNote,magazine):
        count=[0]*26
        for ch in magazine:
            count[ord(ch)-ord('a')]+=1
        for ch in ransomNote:
            count[ord(ch)-ord('a')]-=1
            if count[ord(ch)-ord('a')]<0:
                return False 
        return True 
#Test Case
s=Solution()
print(s.canConstruct("aa","aab"))