def maxProfit(prices) -> int:
    min_price = float('inf')
    max_profit = 0
    total_profit = 0

    for i in range(len(prices) - 1):
        min_price = min(min_price, prices[i])
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)

        if prices[i + 1] < prices[i]:
            total_profit += max_profit
            min_price = prices[i + 1]
            max_profit = 0
        else:
            if i + 1 == len(prices) - 1:
                min_price = min(min_price, prices[i + 1])
                profit = prices[i + 1] - min_price
                max_profit = max(max_profit, profit)
                total_profit += max_profit

    return total_profit


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
