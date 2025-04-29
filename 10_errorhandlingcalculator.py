# ⚠️ Error-Handled Calculator
# Concepts: Try-Except, Input Validation

def calculator():
    print("⚙️ Welcome to the Error-Handled Calculator ⚙️")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            op = input("Choose an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    raise ZeroDivisionError("❌ Cannot divide by zero!")
                result = num1 / num2
            else:
                print("⚠️ Invalid operator.")
                continue

            print(f"✅ Result: {result}\n")

        except ValueError:
            print("❌ Invalid input! Please enter numbers only.\n")
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(f"⚠️ An unexpected error occurred: {e}")

        # Ask if the user wants to continue
        cont = input("Do you want to perform another calculation? (y/n): ").lower()
        if cont != 'y':
            print("👋 Exiting calculator. Goodbye!")
            break

calculator()
