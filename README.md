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

#### Questions-5
Sum of Digit using recursion<br>
Input:123<br>
Output:6

#### Questions-6
Rope Cutting Problem<br>
Length of every piece should be in length of set of {a,b,c}<br>
Return maximum number of cutts<br>
Input:num=5,a=1,b=5,c=3<br>
Output:5

#### Questions-7
Genearte all subset of a string<br>
Input:"AB"<br>
Output:"","A","B","AB"

#### Questions-8
Count all subset whose sum is k<br>
Input:[10,5,2,3,6] k=8<br>
Output:2
