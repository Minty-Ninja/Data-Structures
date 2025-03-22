def insertion(arr): 

    n = len(arr)
    if n<=1: 
        print(arr)

    for i in range(1, n): 
        x = arr[i]
        j = i-1
        while j>=0 and x<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = x


arr= [2, 3, 5, 1, 9, 7, 6, 37, 10, 23567, 789]
insertion(arr)
print(arr)


