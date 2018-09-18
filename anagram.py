import json
dictionarylocation=r'.\words.json'
with open(dictionarylocation, 'r') as f:
    dictionary = json.load(f)

def find(input):
    letters=[]
    for i in input:
        letters.append(i)
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
    return sorted(found, key=lambda x: (-len(x), x))

tryagain=True
while tryagain:
    givenletters=''
    while givenletters=='':
        try:
            print ('What are your letters?')
            givenletters=str(input('')).lower()
        except:
            print ('Just enter your letters.')
    print ('Here are your potential words:')
    found=find(givenletters)
    listdisplay=[]
    length=len(found[0])
    print ("Words of length", length)
    for i in found:
        if len(i)<length:
            print (listdisplay)
            listdisplay=[]
            length=len(i)
            print ("Words of length", length)
        listdisplay.append(i)
        if len(listdisplay)==5:
            print (listdisplay)
            listdisplay=[]

    print ('To continue, hit enter. To exit, type quit and hit enter.')
    quitthis=str(input())
    if quitthis.lower()=='quit' or quitthis.lower()=='exit':
        tryagain=False
