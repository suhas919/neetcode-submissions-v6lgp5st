class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_ = -1
        max_ = 0

        i = 0
        j = 0
        if len(prices) <= 1:
            return 0
        res = 0 
        for p in range(1,len(prices)):
            if prices[p] > prices[i]:
                j = p
                res = max(res,prices[p] - prices[i])

            else:
                i = p

        return res 
            
        