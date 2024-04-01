def maxProfit(prices) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
profit = maxProfit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")

prices = [7, 6, 4, 3, 1]
profit = maxProfit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")

prices = [1, 2, 3, 4, 5, 6]
profit = maxProfit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")
