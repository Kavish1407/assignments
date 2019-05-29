temp=True
lis=[]
while(temp):
    t=input("Enter the tuple ")
    print(t)
    tup=[int(a) for a in t.split()]
    print(tup)

    lis.append(tuple(tup))
    ask=input("Do you want to enter more? y/n ")
    if(ask=='y'):
        temp=True
    else:
        temp=False
print(lis)
lis.sort(key=lambda x: x[-1])
print(lis)

