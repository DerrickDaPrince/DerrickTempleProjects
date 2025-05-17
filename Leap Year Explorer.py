#Task 1 
year = int(input("Enter a year: "))

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year: True")
else:
    print(f"{year} is a leap year: False")
