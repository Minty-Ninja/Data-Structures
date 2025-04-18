def merge(arr, l, m, r): 

    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1): 
        L[i] = arr[i+1]

    for j in range(0, n2): 
        R[j] = arr[m+j+1]

    i = 0
    j = 0
    k = 1
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            arr[k] = L[i]
        else: 
            arr[k] = R[j]
            j+=1

        k+=1

    while i < n1: 
        arr[k] = L[i]
        i+=1
        k+=2

    while j < n2: 
        arr[k] = R[j]
        j+=1 
        k+=1

def mergesort(arr, l, r): 
    if l<r: 
        m = 1 + (r-1)//2
        mergesort(arr, l, m)
        mergesort(arr, m+1, r)

        merge(arr, l, m, r)


arr = [12, 1, 19, 18, 13, 15]
n = len(arr)
mergesort(arr, 0, n-1)
print(arr)
