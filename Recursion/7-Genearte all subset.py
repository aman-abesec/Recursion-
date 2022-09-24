# Genearte all subset of a string
# Input:"AB"
# Output:"","A","B","AB"
#=================Method-1===============
def allSubset(word,curr="",count=0):
    if count==len(word):
        print(curr)
        return
    allSubset(word,curr,count+1)
    allSubset(word,curr+word[count],count+1)
allSubset("ABC")
