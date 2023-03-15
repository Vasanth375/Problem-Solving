# 
#
#   Dynamic programming concept is required to solve this problem, so started learning DP
#
#
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1,2]
prices = [2,4,1]

#priceMap = {prices[i]: i+1 for i in range(len(prices))}
#print(priceMap)

while 1:

    buy = min(prices)

    #print(buy)
    dayOfBuy = prices.index(buy)
    # if dayOfBuy+1 == len(prices):
    #     print(0)

    MaxProfitSell = max(prices[dayOfBuy:])
    print(abs(buy-MaxProfitSell))
    