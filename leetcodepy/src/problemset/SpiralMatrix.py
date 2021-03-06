'''
Created on Oct 1, 2015

@author: mianmianba
'''

class SpiralOrder(object):
    def solution(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        if row == 0: return []
        col = len(matrix[0])
        curIdx = 0
        curJdx = -1
        ret = []
        while row > 0 and col > 0:
            if row == 1:
                for i in range(col):
                    curJdx += 1
                    ret.append(matrix[curIdx][curJdx])
                return ret
            elif col == 1:
                curJdx += 1
                ret.append(matrix[curIdx][curJdx])
                for i in range(row-1):
                    curIdx += 1
                    ret.append(matrix[curIdx][curJdx])
                return ret
            else:
                for i in range(col):
                    curJdx += 1
                    ret.append(matrix[curIdx][curJdx])
                for i in range(row-1):
                    curIdx += 1
                    ret.append(matrix[curIdx][curJdx])
                for i in range(col-1):
                    curJdx -= 1
                    ret.append(matrix[curIdx][curJdx])
                for i in range(row-2):
                    curIdx -= 1
                    ret.append(matrix[curIdx][curJdx])
                row -= 2
                col -= 2
        return ret
                
                
        