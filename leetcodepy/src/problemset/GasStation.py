'''
Created on Sep 2, 2015

@author: mianmianba
'''
class CanCompleteCircuit(object):
    def solution(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        sumGasRmn = 0
        totalGasRmn = 0
        for i in xrange(len(gas)):
            gasRmn = gas[i] - cost[i]
            if sumGasRmn >= 0:
                sumGasRmn += gasRmn
            else:
                sumGasRmn = gasRmn
                start = i
            totalGasRmn += gasRmn
        if totalGasRmn >= 0:
            return start
        else:
            return -1
            