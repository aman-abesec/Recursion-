# Generate all the ways to go from [0,0] to (n-1,n-1) at any cell you can move in four Direction
# L-Left,R-Right,D-Down,U-Up
# Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at
# a cell in the matrix represents that rat can be travel through it.
# Input:arr=[[1,0,0],[1,1,0],[1,1,1]] n=3
# Output:DRDR,DDRR

def solve(r,c,m,n,s,ans):
    m[r][c]=0
    if r==n-1 and c==n-1:
        ans.append("".join(s))
    direction=[[1,0,'D'],[-1,0,'U'],[0,1,'R'],[0,-1,'L']]
    for k in direction:
        x,y,d=r+k[0],c+k[1],k[2]
        if x>=0 and y>=0 and x<n and y<n and m[x][y]==1:
            solve(x,y,m,n,s+[d],ans)
    m[r][c]=1
ans=[]
m=[[1,0,0],[1,1,0],[1,1,1]]
n=3
if m[0][0]==0 or m[n-1][n-1]==0:
    print(-1)
solve(0,0,m,n,[],ans)
print(*ans)
