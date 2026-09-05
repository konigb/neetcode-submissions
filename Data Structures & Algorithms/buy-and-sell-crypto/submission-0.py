class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = i
        
        while j < len(prices):
            res = max(res, prices[j] - prices[i])

            if prices[j] <= prices[i]:
                i = j
            
            j += 1

        return res
        