'''
Created on Sep 15, 2015

@author: mianmianba
'''

class MaxProfit(object):
    def solution(self, prices):
        max_profit = 0
        if len(prices) == 0: return max_profit
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
            