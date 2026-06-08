class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(len(prices)):
            max_profit=max(prices[i:len(prices)])-prices[i]
            if result<max_profit:
                result=max_profit
        return result
        