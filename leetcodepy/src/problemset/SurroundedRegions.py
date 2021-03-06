'''
Created on Sep 19, 2015

@author: mianmianba
'''

class FlipSurroundedRegions(object):
    def expandBFS(self, board, aqueue, visited):
        numRow = len(board)
        numCol = len(board[0])
        while aqueue:
            (row, col) = aqueue.pop()
            visited[row][col] = True
            if row-1 >= 0 and visited[row-1][col] == False and board[row-1][col] == 'O':
                aqueue.append((row-1, col))
            if row+1 < numRow and visited[row+1][col] == False and board[row+1][col] == 'O':
                aqueue.append((row+1, col))
            if col-1 >= 0 and visited[row][col-1] == False and board[row][col-1] == 'O':
                aqueue.append((row, col-1))
            if col+1 < numCol and visited[row][col+1] == False and board[row][col+1] == 'O':
                aqueue.append((row, col+1))
        
    def solutionBFS(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        if numRow == 0: return
        numCol = len(board[0])
        visited = [[False]*numCol for i in range(numRow)]
        aqueue = []
        for i in range(numCol):
            if visited[0][i] == False and board[0][i] == 'X':
                visited[0][i] = True
            else:
                aqueue.append((0, i))
                self.expandBFS(board, aqueue, visited)
        for i in range(numCol):
            if visited[numRow-1][i] == False and board[numRow-1][i] == 'X':
                visited[numRow-1][i] = True
            else:
                aqueue.append((numRow-1, i))
                self.expandBFS(board, aqueue, visited)
        for i in range(1, numRow-1):
            if visited[i][0] == False and board[i][0] == 'X':
                visited[i][0] = True
            else:
                aqueue.append((i, 0))
                self.expandBFS(board, aqueue, visited)
        for i in range(1, numRow-1):
            if visited[i][numCol-1] == False and board[i][numCol-1] == 'X':
                visited[i][numCol-1] = True
            else:
                aqueue.append((i, numCol-1))
                self.expandBFS(board, aqueue, visited)
        for i in range(1, numRow-1):
            for j in range(1, numCol-1):
                if visited[i][j] == False and board[i][j] == 'O':
                    board[i][j] = 'X'

    def expand(self, board, row, col, visited):
        numRow = len(board)
        numCol = len(board[0])
        visited[row][col] = True
        if row-1 >= 0 and visited[row-1][col] == False and board[row-1][col] == 'O':
            self.expand(board, row-1, col, visited)
        if row+1 < numRow and visited[row+1][col] == False and board[row+1][col] == 'O':
            self.expand(board, row+1, col, visited)
        if col-1 >= 0 and visited[row][col-1] == False and board[row][col-1] == 'O':
            self.expand(board, row, col-1, visited)
        if col+1 < numCol and visited[row][col+1] == False and board[row][col+1] == 'O':
            self.expand(board, row, col+1, visited)
        
    def solution(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        numRow = len(board)
        if numRow == 0: return
        numCol = len(board[0])
        visited = [[False]*numCol for i in range(numRow)]
        for i in range(numCol):
            if visited[0][i] == False and board[0][i] == 'X':
                visited[0][i] = True
            else:
                self.expand(board, 0, i, visited)
        for i in range(numCol):
            if visited[numRow-1][i] == False and board[numRow-1][i] == 'X':
                visited[numRow-1][i] = True
            else:
                self.expand(board, numRow-1, i, visited)
        for i in range(1, numRow-1):
            if visited[i][0] == False and board[i][0] == 'X':
                visited[i][0] = True
            else:
                self.expand(board, i, 0, visited)
        for i in range(1, numRow-1):
            if visited[i][numCol-1] == False and board[i][numCol-1] == 'X':
                visited[i][numCol-1] = True
            else:
                self.expand(board, i, numCol-1, visited)
        for i in range(1, numRow-1):
            for j in range(1, numCol-1):
                if visited[i][j] == False and board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                