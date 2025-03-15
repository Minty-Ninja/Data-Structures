#Fibonacci series

def Fib(num):
    if num == 0 or num == 1: 
        return num
    else: 
        return Fib(num-1) + Fib(num-2)
    
print (Fib(5))
     


#Fibonacci series

def Fib(num):
    if num == 0 or num == 1: 
        return num
    else: 
        return Fib(num-1) + Fib(num-2)
    
print (Fib(5))
     

#Factorials

def fact(num): 
    if num == 0 or num == 1: 
        return 1
    else: 
        return num * fact(num-1)
print (fact(4))

#Sum to n
def sum(num):
    if num == 1 or num==0: 
        return num
    else: 
        return num+sum(num-1)
    
print(sum(10))
    

