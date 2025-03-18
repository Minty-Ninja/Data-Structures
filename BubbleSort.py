x = [2, 7, 3, 5, 6, 8, 1]
First = 0
Last = len(x)


for i in range(Last): 
    for j in range(Last-i-1):
        if x[j]>x[j+1]: 
            Temp = x[j]
            x[j] = x[j+1]
            x[j+1] = Temp

print("Corrected List: ", x)


