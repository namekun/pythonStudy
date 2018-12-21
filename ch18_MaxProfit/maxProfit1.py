# input : prices
# output : maxProfit

def maxProfit(prices):
    n = len(prices)
    maxPro = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]

            if profit > maxPro:
                maxPro = profit

    return maxPro


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(maxProfit(stock))
