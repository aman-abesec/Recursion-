# The n-queens puzzle is the problem of placing n queens on an
# n x n chessboard such that no two queens attack each other.
# Input:N=4
# Output:[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

def solveNQueens(n):
    def isValidRow(grid,r,n):
        for i in range(n):
            if grid[r][i]=='Q':return False
        return True

    def isValidCol(grid,c,n):
        for i in range(n):
            if grid[i][c]=='Q':return False
        return True

    def isValidD(grid,r,c,n):
        while r>=0 and c>=0:
            if grid[r][c]=='Q':return False
            r-=1
            c-=1
        return True

    def isValidAnti(grid,r,c,n):
        while r>=0 and c<n:
            if grid[r][c]=='Q':return False
            r-=1
            c+=1
        return True
    def isValid(r,c,grid,n):
        if isValidRow(grid,r,n) and isValidCol(grid,c,n) and isValidD(grid,r,c,n) and isValidAnti(grid,r,c,n):return True
        return False

    def gotAnswer(n,grid,ans):
        ans.append(["".join(k) for k in grid])

    def solve(r,grid,n,ans):
        if r==n:
            gotAnswer(n,grid,ans)
            return
        for i in range(n):
            if isValid(r,i,grid,n):
                grid[r][i]='Q'
                solve(r+1,grid,n,ans)
                grid[r][i]='.'


    ans=[]
    grid=[['.' for _ in range(n)] for __ in range(n)]
    solve(0,grid,n,ans)
    return ans
print(solveNQueens(4))
