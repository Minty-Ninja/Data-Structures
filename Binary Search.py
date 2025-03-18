def BinarySearch(arr, x): 
    left = 0
    right = len(arr)-1
    Found = False

    while left<=right: 
        mid = (left + right)//2

        if arr[mid] == x: 
            print("Element found at: ", mid)
            Found = True
            break
    
        elif arr[mid]<x: 
            left = mid+1
        else:
            right = mid-1

    if not Found: 
        print("Element not found")

arr = [2, 3, 4, 5, 6, 7, 123456789278]
x = 4
BinarySearch(arr, x)
