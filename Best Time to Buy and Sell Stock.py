class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > sell:
                sell = prices[i] - buy
        return sell

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
