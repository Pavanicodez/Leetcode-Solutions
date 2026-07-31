# Leetcode problem 31: Next Permutation
class Solution():
    def nextPermutation(self,arr):
        i=len(arr)-2
        pivot=-1
        # Finding the pivot element
        while(i>=0):
            if(arr[i]<arr[i+1]):
                pivot=i
                break
            i-=1
        i=len(arr)-1
        if(pivot!=-1):
            # swapping least bigger element of pivot with pivot element 
            while(i>pivot):
                if(arr[i]>arr[pivot]):
                    arr[i],arr[pivot]=arr[pivot],arr[i]
                    break
                i-=1
        # Reversing teh elements after pivot 
        left=pivot+1
        right=len(arr)-1
        while(left<right):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
# Test Case
s=Solution()
print(s.nextPermutation([1,7,8,5,9,4,3]))       