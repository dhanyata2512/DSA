num=[3,30,13,14,7,40,20,1,2,6,9]

n=int(input("What number would you like to pick?"))

found=False
for i in range(len(num)):
    if num[i]==n:
        print(f"we found the item at {i} position" )
        found=True
        break
#if found==False:
if not found:    
    print("sorry that number is not in the list...") 

        
