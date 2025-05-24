try:
    num=int(input("Enter the number:"))
except ValueError:
    print("Invalid number!")    

else:
    print("You Entered:",num)