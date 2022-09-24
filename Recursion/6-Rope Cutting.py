# Rope Cutting Problem
# Length of every piece should be in length of set of {a,b,c}
# Return maximum number of cutts
# Input:num=5,a=1,b=5,c=3
# Output:5

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
