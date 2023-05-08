class calculator:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y


c = calculator()
x = 20
y = 10
while True:
    choice = input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n")
    if choice== '5':
        break

    if choice== '1':
        result = c.addition(x, y)
        print("Addition:", result)
    elif choice == '2':
        result = c.subtraction(x, y)
        print("Subtraction:", result)
    elif choice== '3':
        result = c.multiplication(x, y)
        print("multiplication:", result)
    elif choice == '4':
        result = c.division(x, y)
        print("division:", result)
    else:
        print("invalid choice")