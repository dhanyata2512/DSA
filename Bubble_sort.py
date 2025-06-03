surname=['sharma','wong','patel','gautam','hart']

length=len(surname)
for p in range(length-1):
    swapped=False
    for s in range(length-1):
        if surname[s]>surname[s+1]:
            swapped=True