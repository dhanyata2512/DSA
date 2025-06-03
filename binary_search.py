#order=[2,3,4,5,13,14,25,34,35]
order=["d","f","j","p","r","s"]
n=input("What number would you like to pick?")

s=0
e=len(order)-1

# tf=False
# while s<=e:
#     m=(s+e)//2
#     print(f"middle{m};{order[m]}")
#     if n==order[m]:
#         print(f"We found the number at index {m}")
#         tf=True
#         break
#     elif n>order[m]:
#         s=m+1
#     else:
#         e=m-1 

# if tf==False:
#     print("Sorry that number is not in the list...")  

def search_bin(list_search,start,end,search_item):
    if start<=end:
        mid=(start+end)//2
        if list_search[mid]==search_item:
            return mid
        elif list_search[mid]>search_item:
            return search_bin(list_search,start,mid-1,search_item)
        else:
            return search_bin(list_search,mid+1,end,search_item)
    else:
        return -1

value=search_bin(order,s,e,n)
if value==-1:
    print("the item has not been found")
else:
    print(f"the item is at{value}")        


