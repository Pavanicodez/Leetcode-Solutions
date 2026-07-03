# Leetcode problem 121: Best Time to Buy and Sell Stock
class Solution():
    def maxProfit(self,prices):
        i,j=0,1 # i is for buying stock and j is for selling stock
        max_profit=0 
        while j<len(prices):
            if prices[i]>prices[j]: # if buying stock price is more than selling stock price
                i=j # then move i to j index 
                j+=1 # j to its next position
            else:
                max_profit=max(max_profit,prices[j]-prices[i]) # if everything is normal, calculate and update the max profit
                j+=1 
        return max_profit
s=Solution()
print(s.maxProfit([2,1,2,1,0,1,2]))