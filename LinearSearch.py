list = [4, 3, 67, 87654, 234, 5432345, 454, 23456, 4565,458,84,85,88544]
x = int(input("Please enter a number"))
Found = False
Counter = 0

for i in range(12):
    if x == list[Counter]: 
        Found = True

    else: 
        Counter+=1

if Found:
    print("Number found at index: ", Counter)
else: 
    print("Number not found")

