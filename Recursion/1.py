# Print N to 1 Number Using recursion.
# Input:10
# Output:10 9 8 7 6 5 4 3 2 1

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
