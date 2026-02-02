def sumOfArr(arr):
    total=0
    for element in arr:
        total += element

    return total    
arr=[11,22,33,44,55,66,77,88,99,00]
result=sumOfArr(arr)
print("Sum of array:",result)