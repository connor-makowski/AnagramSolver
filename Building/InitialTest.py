dictionary={'a':["apple","atom"], 'b':["banana", "bat"], 'e':[], 'l':[], 'm':[], 'o':[], 'p':[], 't':[]}

def find(letters):
    consider=[]
    found=[]
    for i in list(set(letters)):
        for j in dictionary[i]:
            consider.append(j)
    letters.append("")
    for i in consider:
        ileft=i
        for j in letters:
            if len(ileft)==0:
                found.append(i)
                break
            if j in i:
                ileft=ileft.replace(j,"",1)
    return found

x=find(["a","t","o","m"])
print (x)
