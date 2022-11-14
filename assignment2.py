def calculate_area_of_circle(radius: float) -> float: 
    return (22/7.0) * radius**2

print("Welcome to my area of a circle calculation application. Enter q or quit to exit the program.\n")

while True:
    try:
        user_input = str(input("Enter the radius of the circle: "))

        if user_input == "quit" or user_input == "q":
            break
        
        radius = float(user_input)
        print(f"The area of the circle of radius {radius} is {calculate_area_of_circle(radius)}")

    except:
        print("invalid input, enter a number for the radius of the circle")