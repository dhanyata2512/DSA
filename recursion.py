n=int(input("What number do you want to find the factorial of"))

# add=0

# for i in range(1,n+1):
#     add=i+add
# print(add)

# def total(n):
#     if n == 1:
#         return 1
#     else:
#         return n+total(n-1)
# print(total(n)) 

# def fibo(n):
#     if n==0 or n==1:
#         return n
#     else:
#          return fibo(n-1) + fibo(n-2)
# print(fibo(n)) 

def factorial(n):
    if n==1:
        return n
    else:
        return factorial(n-1)*n
print(factorial(n))    


    
