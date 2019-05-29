
def binarysearch(numbs,element,l,r):
    while(l<=r):
        mid=int((l+r)/2)
        #print (mid)
        if numbs[mid]==element:
            return mid
        elif numbs[mid] > element:
            r=mid-1
        else:
            l=mid+1
    return -1




x = input("Enter the elements ")
numbers=[int(a) for a in x.split()]
y=int(input("Enter element to find "))
index=binarysearch(numbers,y,0,(len(numbers)-1))
if index==-1:
    print("Element not found")
else:
    print("index is "+str(index))