def addition(number_1, number_2):
    return number_1 + number_2


def subtraction(number_1, number_2):
    return number_1 - number_2


def multiplication(number_1, number_2):
    return number_1 * number_2


def division(number_1, number_2):
    return number_1 / number_2


print("Select operation.")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
while True:
    choice = input("Enter choice(a/b/c/d): ")
    number_1 = int(input("Please enter the first number: "))
    number_2 = int(input("Please enter the second number: "))
    if choice == 'a':
        print(number_1, " + ", number_2, " = ", addition(number_1, number_2))

    elif choice == 'b':
        print(number_1, " - ", number_2, " = ", subtraction(number_1, number_2))

    elif choice == 'c':
        print(number_1, " * ", number_2, " = ", multiplication(number_1, number_2))
    elif choice == 'd':
        print(number_1, " / ", number_2, " = ", division(number_1, number_2))
    else:
        print("This is an invalid input")
