import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    if num in memo:
        return memo[num]
        
    elif num == 0:
        memo[num] = 0
        return 0
    elif num == 1:
        memo[num] = 1
        return 1
    else:
        memo[num] = fibonacci(num-1) + fibonacci(num-2)
        return fibonacci(num-1) + fibonacci(num-2)
        

memo={} #global dictionary to store the fibonacci number already computed
print("Fibonacci number:",fibonacci(50))