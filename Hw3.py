def count(num): 
    if num == 1: 
        print(1)
    else: 
        print(num)
        count(num-1)

count(6)