# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



class Solution(object):
    def maxProfit(self, prices):
        l,r = 0,1  #left(l) = buy, right(r) = sell
        MaxP = 0   #default case
        # This while loop will keep iterating through prices while the right pointer has not passed the end of prices
        while r < len(prices):
            # checks to see if profitable, this sees if the prices of the left is less than the prices om the right
            if prices[l] < prices[r]:
                # Calculate if profitable or not
                MadeMoney = prices[r] - prices[l]
                MaxP = max(MaxP,MadeMoney)
            else:
                # We want the left pointer to be at the minimum, thats why we set it equal to right pointer
                #if the left price is not lower than the right we want to shift it all the way to the right indicating we found the lowest price
                l = r
            r += 1
        return MaxP
