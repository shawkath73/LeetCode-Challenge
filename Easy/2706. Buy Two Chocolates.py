class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        prices = prices[0] + prices[1]
        if prices <= money:
            money-=prices
        return money         