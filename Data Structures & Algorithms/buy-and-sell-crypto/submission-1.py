class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        low = 101
        high = 0


        for i in range (len(prices)):
            if (prices[i] < low):
                low = prices[i]
                high = 0
            elif (prices[i] > high):
                high = prices[i]
            maxi = max(maxi, (high - low))

        return maxi

            

        
            
            


        