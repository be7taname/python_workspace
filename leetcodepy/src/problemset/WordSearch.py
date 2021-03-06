'''
Created on Oct 1, 2015

@author: mianmianba
'''

class Exist(object):
    def existWord(self, board, word, row, col, visited):
        numRow = len(board)
        numCol = len(board[0])
        wordLen = len(word)
        if wordLen == 1:
            if row > 0 and visited[row-1][col] == False and board[row-1][col] == word:
                return True
            if row < numRow-1 and visited[row+1][col] == False and board[row+1][col] == word:
                return True
            if col > 0 and visited[row][col-1] == False and board[row][col-1] == word:
                return True
            if col < numCol-1 and visited[row][col+1] == False and board[row][col+1] == word:
                return True
            return False
        else:
            cc = word[0]
            if row > 0 and visited[row-1][col] == False and board[row-1][col] == cc:
                visited[row-1][col] = True
                if self.existWord(board, word[1:], row-1, col, visited): return True
                visited[row-1][col] = False
            if row < numRow-1 and visited[row+1][col] == False and board[row+1][col] == cc:
                visited[row+1][col] = True
                if self.existWord(board, word[1:], row+1, col, visited): return True
                visited[row+1][col] = False
            if col > 0 and visited[row][col-1] == False and board[row][col-1] == cc:
                visited[row][col-1] = True
                if self.existWord(board, word[1:], row, col-1, visited): return True
                visited[row][col-1] = False
            if col < numCol-1 and visited[row][col+1] == False and board[row][col+1] == cc:
                visited[row][col+1] = True
                if self.existWord(board, word[1:], row, col+1, visited): return True
                visited[row][col+1] = False
            return False
        
    def solution(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        numRow = len(board)
        numCol = len(board[0])
        wordLen = len(word)
        visited = [[False for x in range(numCol)] for y in range(numRow)]
        for row in range(numRow):
            for col in range(numCol):
                if board[row][col] == word[0]:
                    if wordLen == 1: return True
                    else: 
                        visited[row][col] = True
                        if self.existWord(board, word[1:], row, col, visited): return True
                        visited[row][col] = False
        return False
    