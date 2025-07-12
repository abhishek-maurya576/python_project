while True:
    try:
        num1 = int(input("Enter a first number: "))
        num2 = int(input("Enter a second number: "))

        print("Enter an operation\n+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division\nq for exit")
        o = input("Enter an Operation: ")
        match o:
            case "+":
                print(f"The sum is: {num1+num2}")
            case "-":
                print(f"The sum is: {num1-num2}")
            case "*":
                print(f"The sum is: {num1*num2}")
            case "/":
                print(f"The sum is: {num1/num2}")
            case "q":
                break
            case default:
                print("There is an error!")
    except Exception as e:
        print("There is something error occured\n",e)