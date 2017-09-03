def stockPrice(arr):
    min_stock_price = arr[0]
    max_profit = 0

    for price in arr:
        min_stock_price = min(min_stock_price,price)

        comparision_profit = price - min_stock_price

        max_profit = max(max_profit, comparision_profit)
    return max_profit


arr = [23 ,12, 3, 10]
print(stockPrice(arr))

