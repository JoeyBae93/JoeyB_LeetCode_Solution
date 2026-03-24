class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Runtime: 30 ms (Beats 94.29%) | Memory: 19.06 mb (Beats 69.78%)
        """
        # declare minimum price and maximum profit variables
        minPrice      = float('inf')
        maxProfit     = 0

        # loop through the prices array to find the best time to buy and sell
        for price in prices:
            # if current price is lower than the miminum price, update price to mimimum price
            if price < minPrice:
                minPrice = price

            # calculate the current profit
            currentProfit = price - minPrice

            # if current profit is larger than the max profit, update the max profit to current profit
            if currentProfit > maxProfit:
                maxProfit = currentProfit

        # return max profit
        return maxProfit