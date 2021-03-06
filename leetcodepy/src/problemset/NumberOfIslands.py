'''
Created on Sep 4, 2015

@author: mianmianba
'''
class NumIslands(object):
    def solutionDFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numRow = len(grid)
        if numRow == 0:
            return 0
        numCol = len(grid[0])
        cnt = 0
        visited = [[False for x in range(numCol)] for x in range(numRow)]
        for i in xrange(numRow):
            for j in xrange(numCol):
                if grid[i][j] == '1' and visited[i][j] == False:
                    self.visitIsland(grid, visited, i, j)
                    cnt+=1
        return cnt
                
    def visitIsland(self, grid, visited, rowId, colId):
        numRow = len(grid)
        numCol = len(grid[0])
        visited[rowId][colId] = True
        if (rowId+1)<numRow and grid[rowId+1][colId] == '1' and visited[rowId+1][colId] == False:
            self.visitIsland(grid, visited, rowId+1, colId)
        if (rowId-1)>=0 and grid[rowId-1][colId] == '1' and visited[rowId-1][colId] == False:
            self.visitIsland(grid, visited, rowId-1, colId)
        if (colId+1)<numCol and grid[rowId][colId+1] == '1' and visited[rowId][colId+1] == False:
            self.visitIsland(grid, visited, rowId, colId+1)
        if (colId-1)>=0 and grid[rowId][colId-1] == '1' and visited[rowId][colId-1] == False:
            self.visitIsland(grid, visited, rowId, colId-1)
            
    def solutionBFS(self, grid):
        numRow = len(grid)
        if numRow == 0:
            return 0
        numCol = len(grid[0])
        visited = [[False for x in range(numCol)] for x in range(numRow)]
        que = []
        cnt = 0
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j] == '1' and visited[i][j] == False:
                    que.append([i,j])
                    visited[i][j] = True
                    while que:
                        rowId = que[0][0]
                        colId = que[0][1]
                        que.pop(0)
                        if rowId+1<numRow and grid[rowId+1][colId] == '1' and visited[rowId+1][colId] == False:
                            que.append([rowId+1, colId])
                            visited[rowId+1][colId] = True
                        if rowId-1>=0 and grid[rowId-1][colId] == '1' and visited[rowId-1][colId] == False:
                            que.append([rowId-1, colId])
                            visited[rowId-1][colId] = True
                        if colId+1<numCol and grid[rowId][colId+1] == '1' and visited[rowId][colId+1] == False:
                            que.append([rowId, colId+1])
                            visited[rowId][colId+1] = True
                        if colId-1>=0 and grid[rowId][colId-1] == '1' and visited[rowId][colId-1] == False:
                            que.append([rowId, colId-1])
                            visited[rowId][colId-1] = True
                    cnt += 1
        return cnt
