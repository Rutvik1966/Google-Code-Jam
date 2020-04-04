from sys import stdin,stdout
from collections  import Counter
n =int(stdin.readline().strip())
results=[]
for i in range(n):
    d=int(stdin.readline().strip())
    flist=[]
    k=0
    r=0
    c=0
    for j in range(d):
        listrow=list(map(int,stdin.readline().strip().split()))
        flist.append(listrow)
        duplist=[item for item,count in Counter(listrow).items() if count>1]
        if(len(duplist)>=1):
            r+=1
    for number in range(len(flist)):
        k+=flist[number][number]
    listcol=[]
    flistnew=[num for list_ in flist for num in list_]
    for thing in range(d):
        templist=[]
        index=thing
        
        for a in range(d):
            templist.append(flistnew[index])
            index+=d
        listcol.append(templist)
        duplistC=[item for item,count in Counter(templist).items() if count>1]
        if(len(duplistC)>=1):
            c+=1
    templist2=[]
    templist2.append(i+1)
    templist2.append(k)
    templist2.append(r)
    templist2.append(c)
    results.append(templist2)
for list_ in results:
    print("Case #{}: {} {} {}".format(list_[0], list_[1],list_[2],list_[3]))