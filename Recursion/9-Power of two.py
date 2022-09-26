# Given number is power of 2 or not
# Input:256
# Output:Return True
def isPowerof2(n):
    if n==1:return True
    if n%2!=0 or n<=0:return False
    return isPowerof2(n//2)
print(isPowerof2(257))

# Note:>The question power of three and 4 are same as this problem
