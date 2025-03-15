#Fibonacci series

def Fib(num):
    if num == 0 or num == 1: 
        return num
    else: 
        return Fib(num-1) + Fib(num-2)
    
print (Fib(5))
     
