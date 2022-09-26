# Given a N*N board with the Knight placed on the first
# block of an empty board. Moving according to the rules of chess
# knight must visit each square exactly once.
# Print the order of each cell in which they are visited.
# Input:>n=8
# Output:>[[0, 59, 38, 33, 30, 17, 8, 63], [37, 34, 31, 60, 9, 62, 29, 16], [58, 1, 36, 39, 32, 27, 18, 7], [35, 48, 41, 26, 61, 10, 15, 28], [42, 57, 2, 49, 40, 23, 6, 19], [47, 50, 45, 54, 25, 20, 11, 14], [56, 43, 52, 3, 22, 13, 24, 5], [51, 46, 55, 44, 53, 4, 21, 12]]

def isValid(r,c,N):
    if (r>=0 and c>=0 and r<N and c<N):return True
    return False

def solve(r,c,N,grid,count):
    if count==N**2:
        return True
    d=[[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    for k in d:
        x,y=r+k[0],c+k[1]
        if isValid(x,y,N) and grid[x][y]==-1:
            grid[x][y]=count
            if solve(x,y,N,grid,count+1):
                return True
            grid[x][y]=-1
    return False
N=8
grid=[[-1 for _ in range(N)] for __ in range(N)]
grid[0][0]=0
solve(0,0,N,grid,1)
print(grid)
