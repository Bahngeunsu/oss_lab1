
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

print("Select operation")
print("1.Add")
print("2.Subtract")

choice = input("Enter choice(1/2)")
num1 = float(input("first num:"))
num2 = float(input("second num:"))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))

else:
    print("wrong")
    
