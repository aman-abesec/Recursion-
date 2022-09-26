# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
# the number could represent. Return the answer in any order.
# Input:digits="23"
# Output:["ad","ae","af","bd","be","bf","cd","ce","cf"]

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
