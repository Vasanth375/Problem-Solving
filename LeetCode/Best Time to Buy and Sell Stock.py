prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
# prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]

left = 0    # buy pointer
right = 1   # sell pointer
maxCOunt = 0
# Two Pointer Approach
while right < len(prices):
    # Checking if selling cost greater than Buying Cost
    if prices[left] < prices[right]:
        if abs(prices[left] - prices[right]) > maxCOunt:
            # then counting it as a max profit
            maxCOunt = abs(prices[left] - prices[right])
        # so left isn't incrementing because left is now min buying price
        right += 1
    else:
        # condition will come here if buying price is greater then selling price
        # so we just pointing to the left to the current right pointer
        # incrementing the right pointer
        left = right
        right += 1
print(maxCOunt)
