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
   # print(array)
    
def merge_sort(array,low,high):
    if low < high:
        middle=(low+high)//2
        merge_sort(array,low,middle)
        merge_sort(array,middle+1,high)
        merge(array,low,middle,high)        


list=[3,9,4,6,5,8,7,13,12,14,10]
merge_sort(list,0,len(list)-1)
print(list)

print(list)
