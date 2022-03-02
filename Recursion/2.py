# Print 1 to N Number Using recursion.
# Input:10
# Output:1 2 3 4 5 6 7 8 9 10

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
