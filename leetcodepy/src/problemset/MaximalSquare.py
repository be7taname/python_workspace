'''
Created on Sep 27, 2015

@author: mianmianba
'''

class MaximalSquare(object):
    def solution(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        numRow = len(matrix)
        if numRow == 0: return 0
        numCol = len(matrix[0])
        sqrSize = [[0 for x in range(numCol)] for y in range(numRow)]
        maxSqr = 0
        for i in range(numRow):
            for j in range(numCol):
                if i == 0:
                    if matrix[0][j] == '1': sqrSize[0][j] = 1
                elif j == 0: 
                    if matrix[i][0] == '1': sqrSize[i][0] = 1
                else:
                    if matrix[i][j] == '1':
                        sqrSize[i][j] = 1 + min(sqrSize[i-1][j], sqrSize[i][j-1], sqrSize[i-1][j-1])
                if sqrSize[i][j] > maxSqr:
                    maxSqr = sqrSize[i][j]
        return maxSqr*maxSqr
    
                    