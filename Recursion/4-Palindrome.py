# Palindrome Cheque using recursion
# Input:"ABBC"
# Output:True

#=================Method-1===============
def isPalindrome(word,start,end):
    if start>=end:
        return True
    if word[start]!=word[end]:
        return False
    return isPalindrome(word,start+1,end-1)
word="AABD"
print(isPalindrome(word,0,len(word)-1))

#======================Method-2============
def isPalindrome(word,start,end):
    if start>=end:
        return True
    return word[start]==word[end] and isPalindrome(word,start+1,end-1)
word="ABC"
print(isPalindrome(word,0,len(word)-1))
