print("Welcome to my calculator application. Input quit or q to exit the application instead of the math equation (x*y/z).\n\n")

while True:
    math_equation = str(input("Enter you math expression: "))
    
    if math_equation == "quit" or math_equation == "q":
        break
    
    try:
        answer = eval(math_equation)
        print(f"{math_equation}= {answer}")
    except:
        print("invalid input")