import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Square Root (√)")
        print("7. Trigonometric Functions")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("Result:", result)
        elif choice == '2':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print("Result:", result)
        elif choice == '3':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 * num2
            print("Result:", result)
        elif choice == '4':
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print("Result:", result)
        elif choice == '5':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = base ** exponent
            print("Result:", result)
        elif choice == '6':
            num = float(input("Enter the number: "))
            result = math.sqrt(num)
            print("Result:", result)
        elif choice == '7':
            print("\nSelect a trigonometric function:")
            print("1. Sine (sin)")
            print("2. Cosine (cos)")
            print("3. Tangent (tan)")
            print("4. Arcsine (asin)")
            print("5. Arccosine (acos)")
            print("6. Arctangent (atan)")

            trig_choice = input("Enter your choice (1-6): ")

            num = float(input("Enter the angle in degrees: "))

            if trig_choice == '1':
                result = math.sin(math.radians(num))
                print("Result:", result)
            elif trig_choice == '2':
                result = math.cos(math.radians(num))
                print("Result:", result)
            elif trig_choice == '3':
                result = math.tan(math.radians(num))
                print("Result:", result)
            elif trig_choice == '4':
                result = math.degrees(math.asin(num))
                print("Result:", result)
            elif trig_choice == '5':
                result = math.degrees(math.acos(num))
                print("Result:", result)
            elif trig_choice == '6':
                result = math.degrees(math.atan(num))
                print("Result:", result)
            else:
                print("Invalid choice! Please try again.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

scientific_calculator()
