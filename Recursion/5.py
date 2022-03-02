# Sum of Digit using recursion
# Input:123
#Output:6

#=================Method-1===============
def sumOfDigit(num):
    if num==0:
        return 0
    return num%10+sumOfDigit(num//10)
print(sumOfDigit(1))
