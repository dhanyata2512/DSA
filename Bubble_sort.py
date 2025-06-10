surname=['sharma','wong','patel','gautam','hart']

length=len(surname)
for p in range(length):
    swapped=False
    print('pass=',p)
    for s in range(length-1):
        if surname[s]>surname[s+1]:
            swapped=True
            surname[s],surname[s+1]=surname[s+1],surname[s]
            # temp=surname[s]
            # surname[s]=surname[s+1]
            # surname[s+1]=temp
            print(surname)
    if not swapped:
        break
    print(surname)
