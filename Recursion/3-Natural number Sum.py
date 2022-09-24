# Return Natural number Sum using recursion
# Input:5
# Explanation:1 + 2 + 3 + 4 + 5
# Output:15

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
