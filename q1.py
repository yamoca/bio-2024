firstnum = int(input("enter start int (n)"))
i = int(input("enter digit to find (i)"))

collecteddata = ""

currentnum = firstnum
while len(collecteddata) < i:
    collecteddata += str(currentnum)
    currentnum += 1



print(collecteddata[i-1])