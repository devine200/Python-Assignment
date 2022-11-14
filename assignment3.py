import time
print("Enter your information below")

name = str(input("Enter your name: "))
try:
    age = int(input("Enter your age: "))
except:
    print("invalid input")

department = str(input("Enter you department: "))

print("\ndetails loading........")
time.sleep(2)
print(f"\nName: {name}\nAge: {age}\nDepartment: {department}")