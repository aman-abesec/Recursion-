# Count all subset whose sum is k
# Input:[10,5,2,3,6] k=8
# Output:2
#=================Method-1===============
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
