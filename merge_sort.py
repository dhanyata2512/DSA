def merge(array,low,mid,high):
    temp=[]
    start1=low
    start2=mid+1
    while start1 <= mid and start2 <= high: #as long as both arrays have items
        if array[start1]< array[start2]:
            temp.append(array[start1])
            start1=start1 +1
        else:
            temp.append(array[start2])
            start2=start2+1

    while start1 <= mid:
        temp.append(array[start1])
        start1= start1+1
    while start2 <= high:
        temp.append(array[start2])
        start2=start2+1
    
    pos=0
    for i in range(low,high+1):
        array[i]=temp[pos]
        pos=pos+1
    print(array)
list=[3,9,4,6,5,8]
merge(list,2,3,5)

print(list)