# Recursion
## Recursion Questions Input and Output.

#### Questions-1
Print N to 1 Number Using recursion.<br>
Input:10<br>
Output:10 9 8 7 6 5 4 3 2 1

```python
#=================Method-1===============
def printNto1(num):
    if num==0:
        return
    print(num,end=" ")
    printNto1(num-1)
printNto1(10)

#======================Method-2============
def printNto1(num,s=1):
    if s>num:
        return
    printNto1(num,s+1)
    print(s,end=" ")
printNto1(15)
```

#### Questions-2
Print 1 to N Number Using recursion.<br>
Input:10<br>
Output:1 2 3 4 5 6 7 8 9 10
```python
#=================Method-1===============
def print1toN(num):
    if num==0:
        return
    print1toN(num-1)
    print(num,end=" ")
print1toN(10)

#======================Method-2============
def print1toN(num,s=1):
    if s>num:
        return
    print(s,end=" ")
    print1toN(num,s+1)
print1toN(15)
```

#### Questions-3
Return Natural number Sum using recursion<br>
Input:5<br>
Explanation:1 + 2 + 3 + 4 + 5<br>
Output:15
```python
#=================Method-1===============
def SumOfNatural(num):
    if num==1:
        return 1
    return num+SumOfNatural(num-1)
print(SumOfNatural(8))

#======================Method-2============
def SumOfNatural(num,c=1):
    if num==c:
        return c
    return c+SumOfNatural(num,c+1)
print(SumOfNatural(5))
```

#### Questions-4
Palindrome Cheque using recursion<br>
Input:"ABBC"<br>
Output:True
```python
#=================Method-1===============
def isPalindrome(word,start,end):
    if start>=end:
        return True
    if word[start]!=word[end]:
        return False
    return isPalindrome(word,start+1,end-1)
word="AABD"
print(isPalindrome(word,0,len(word)-1))

#======================Method-2============
def isPalindrome(word,start,end):
    if start>=end:
        return True
    return word[start]==word[end] and isPalindrome(word,start+1,end-1)
word="ABC"
print(isPalindrome(word,0,len(word)-1))
```

#### Questions-5
Sum of Digit using recursion<br>
Input:123<br>
Output:6
```python
#=================Method-1===============
def sumOfDigit(num):
    if num==0:
        return 0
    return num%10+sumOfDigit(num//10)
print(sumOfDigit(1))
```

#### Questions-6
Rope Cutting Problem<br>
Length of every piece should be in length of set of {a,b,c}<br>
Return maximum number of cutts<br>
Input:num=5,a=1,b=5,c=3<br>
Output:5
```python
#=================Method-1===============
def maxRope(num,a,b,c):
    if num==0:
        return 0
    if num<0:
        return -1
    res=max(maxRope(num-a,a,b,c),maxRope(num-b,a,b,c),maxRope(num-c,a,b,c))
    if res==-1:
        return -1
    return res+1
print(maxRope(5,1,5,3))#5
print(maxRope(23,12,9,11))#2
print(maxRope(5,4,2,6))#-1
```

#### Questions-7
Genearte all subset of a string<br>
Input:"AB"<br>
Output:"","A","B","AB"
```python
#=================Method-1===============
def allSubset(word,curr="",count=0):
    if count==len(word):
        print(curr)
        return
    allSubset(word,curr,count+1)
    allSubset(word,curr+word[count],count+1)
allSubset("ABC")
```

#### Questions-8
Count all subset whose sum is k<br>
Input:[10,5,2,3,6] k=8<br>
Output:2
```python
count=0
def countSubSet(l,k,sub=[],size=0):
    if size==len(l):
        if sum(sub)==k:
            return 1
        return 0
    return countSubSet(l,k,sub,size+1)+countSubSet(l,k,sub+[l[size]],size+1)
print(countSubSet([1,2,3],4))
print(countSubSet([10,20,15],25))
print(countSubSet([10,5,2,3,6],8))
print(countSubSet([1,2,39],4))
```

#### Question-9
Given number is power of 2 or not<br>
Input:256<br>
Output:Return True
```python
def isPowerof2(n):
    if n==1:return True
    if n%2!=0 or n<=0:return False
    return isPowerof2(n//2)
print(isPowerof2(257))
```

#### Question-10
Find all possible combination of number from a given array that sum is target<br>
Input:nums=[2,3,5] target=8<br>
Output:[[2,2,2,2],[2,3,3],[3,5]]
```python
ans=[]
def combinationSum(arr,target,i,l,num):
    global ans
    if target<0:return
    if i==l:
        if target==0:
            ans.append(num)
        return
    if target-arr[i]>=0:
        combinationSum(arr,target-arr[i],i,l,num+[arr[i]])
    combinationSum(arr,target,i+1,l,num)
combinationSum([2,4,5],6,0,3,[])
print(ans)
```

#### Question-11
Generate all the ways to go from [0,0] to (n-1,n-1) at any cell you can move in four Direction<br>
L-Left,R-Right,D-Down,U-Up<br>
Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at<br>
a cell in the matrix represents that rat can be travel through it.<br>
Input:arr=[[1,0,0],[1,1,0],[1,1,1]] n=3<br>
Output:DRDR,DDRR
```python
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
```

#### Question-12
The n-queens puzzle is the problem of placing n queens on an<br>
n x n chessboard such that no two queens attack each other.<br>
Input:N=4<br>
Output:[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```python
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
```

#### Question-13
    Write a program to solve a Sudoku puzzle by filling the empty cells.
    A sudoku solution must satisfy all of the following rules:
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells.
    Input:grid=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Output:[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
```python
def solveSudoku(grid):
    def isValid(r,c,val,grid):
        for i in range(9):
            if grid[r][i]==val:return False
            if grid[i][c]==val:return False
            if grid[3*(r//3)+i//3][3*(c//3)+i%3]==val:return False
        return True

    def solve(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j]==".":
                    for k in range(1,10):
                        if isValid(i,j,str(k),grid):
                            grid[i][j]=str(k)
                            if solve(grid)==True:
                                return True
                            else:
                                grid[i][j]="."
                    return False
        return True
    solve(grid)
    print(grid)
solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])

```

#### Question-14

Given a N*N board with the Knight placed on the first<br>
block of an empty board. Moving according to the rules of chess<br>
knight must visit each square exactly once.<br>
Print the order of each cell in which they are visited.<br>
Input:>n=8<br>
Output:>[[0, 59, 38, 33, 30, 17, 8, 63], [37, 34, 31, 60, 9, 62, 29, 16], [58, 1, 36, 39, 32, 27, 18, 7], [35, 48, 41, 26, 61, 10, 15, 28], [42, 57, 2, 49, 40, 23, 6, 19], [47, 50, 45, 54, 25, 20, 11, 14], [56, 43, 52, 3, 22, 13, 24, 5], [51, 46, 55, 44, 53, 4, 21, 12]]

```python
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
```

#### Question-15
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that<br>
the number could represent. Return the answer in any order.<br>
Input:digits="23"<br>
Output:["ad","ae","af","bd","be","bf","cd","ce","cf"]
```python
def solve(h_map,stack,digits,l,c,result):
    if digits=="":return []
    if l==c:
        result.append("".join(stack))
        return
    for i in h_map[int(digits[c])]:
        stack.append(i)
        solve(h_map,stack,digits,l,c+1,result)
        stack.pop()

digits="23"
h_map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
result=[]
stack=[]
solve(h_map,stack,digits,len(digits),0,result)
print(result)
```

#### Question-16
Given a collection of candidate numbers (candidates) and a target number (target),<br>
find all unique combinations in candidates where the candidate numbers sum to target.<br>
Each number in candidates may only be used once in the combination.<br>
Note: The solution set must not contain duplicate combinations.<br>

Input:arr=[10,1,2,7,6,1,5] target=8<br>
Output:[[1,1,6],[1,2,5],[1,7],[2,6]]
```python
def combinationSum2(candidates,target):
    def solve(result,stack,c,candidates,target,l):
        if target==0:
            result.append([m for m in stack])
            return
        if c==l:return
        for i in range(c,l):
            if i>c and candidates[i]==candidates[i-1]:continue
            if target-candidates[i]>=0:
                stack.append(candidates[i])
                solve(result,stack,i+1,candidates,target-candidates[i],l)
                stack.pop()
    result=[]
    stack=[]
    candidates.sort()
    l=len(candidates)
    solve(result,stack,0,candidates,target,l)
    return result
candidates=[10,1,2,7,6,1,5]
target=8
print(combinationSum2(candidates,target))
```
