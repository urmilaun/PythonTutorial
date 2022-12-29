def swaplist(newList):
    size=len(newList)
    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp
    return newList
newList=[10,20,30,40,50]
print(swaplist(newList))