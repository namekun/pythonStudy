def maxProfit(prices):
    n = len(prices)
    maxPro = 0
    minPrice = prices[0]

    for x in range(1, n):
        profit = prices[x] - minPrice
        if profit > maxPro:
            maxPro = profit

        if prices[x] < minPrice:
            minPrice = prices[x]

    return maxPro


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxProfit(stock))
