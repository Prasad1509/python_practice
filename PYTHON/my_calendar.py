import calendar

year = int(input("Enter the Year: ")) 
month = int(input("Enter the Month: "))
 
cal = calendar.month(year, month) 
print(cal)
