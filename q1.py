firstnum = int(input("enter start int (n)"))
i = int(input("enter digit to find (i)"))

data = []
collecteddata = ""
for j in range(i):
    collecteddata+= str(firstnum+j)
    if len(collecteddata) == i:
        break




print(collecteddata[i-1])