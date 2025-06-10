numbers=[4,3,6,9,2,8,13,14]

length=len(numbers)
for i in range(length):
    key=numbers[i]
    j=i-1
    while j >= 0 and key < numbers[j]:
        numbers[j+1]=numbers[j]
        j=j-1
    numbers[j+1]=key
    print(numbers)