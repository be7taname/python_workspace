'''
Created on Sep 8, 2015

@author: mianmianba
'''
class MinimumTotal(object):
    def solution(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        numRows = len(triangle)
        pathsum = [0] * numRows
        pathsum[0] = triangle[0][0]
        for row in range(1, numRows):
            for col in range(row, -1, -1):
                if col == row:
                    pathsum[col] = pathsum[col-1] + triangle[row][col]
                elif col == 0:
                    pathsum[col] += triangle[row][col]
                else:
                    pathsum[col] = (pathsum[col] if pathsum[col] <= pathsum[col-1] else pathsum[col-1]) \
                    + triangle[row][col]
        return min(pathsum)
    