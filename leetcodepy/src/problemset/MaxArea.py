'''
Created on Sep 1, 2015

@author: mianmianba
'''

class MaxArea(object):
    def solution(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        curMaxArea = (j - i) * min(height[i], height[j])
        while (i < j):
            if (height[i] < height[j]):
                i += 1
                while ((height[i] <= height[i-1]) and (i < j)):
                    i += 1
            else:
                j -= 1
                while ((height[j] <= height[j+1]) and (j > i)):
                    j-= 1
            thisArea = (j - i) * min(height[i], height[j])
            if (thisArea > curMaxArea):
                curMaxArea = thisArea
        return curMaxArea
