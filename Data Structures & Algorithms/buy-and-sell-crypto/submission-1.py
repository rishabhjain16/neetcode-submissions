class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy,sell = 0,1
        while sell<len(prices):
            # profitable transaction
            if prices[buy]<prices[sell]:
                profit = prices[sell]-prices[buy]
                prof=max(prof,profit)
            else:
                buy=sell
            sell = sell +1
        return prof

