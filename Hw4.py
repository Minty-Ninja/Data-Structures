x= int(input("How many elements do you want?"))
arr=[]
for i in range(x): 
    y = int(input("Number: "))
    arr.append(y)

#Algorithms
def Sort(arr): 
    for i in range(len(arr)): 
        for j in range(len(arr)-i-1): 
            if arr[j]>arr[j+1]: 
                Temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = Temp

Sort(arr)
print("Corrected List: ", arr)

target = int(input("Select target element: "))

def BinarySearch(arr, target): 
    left = 0
    right = len(arr)-1
    Found = False

    while left<=right: 
        mid = (left + right)//2

        if arr[mid] == target: 
            print("Element found at: ", mid)
            Found = True
            break

        elif arr[mid]< target: 
            left= mid+1
        
        else: 
            right = mid-1

    if not Found: 
        print("Element not found")

BinarySearch(arr, target)