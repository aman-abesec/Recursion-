# Find all possible combination of number from a given array that sum is target
# Input:nums=[2,3,5] target=8
# Output:[[2,2,2,2],[2,3,3],[3,5]]

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
