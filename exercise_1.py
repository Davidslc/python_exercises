while True:
    try:
        num_1 = int(input("Please enter first integer "))
        break
    except ValueError:
        print("That is not a valid entry. Try again")

while True:
    try:
        num_2 = float(input("Please enter second integer "))
        break
    except ValueError:
        print("That is not a valid entry. Try again")

summed = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2


def try_divide():
    try:
        quotient = num_1 / num_2
        remainder = num_1 % num_2
        print("The quotient of %d and %d is: %d with remainder: %d " % (num_1, num_2, quotient, remainder))
    except ZeroDivisionError:
        print("There is no quotient, because you cannot divide by zero")
    finally:
        print("What?")


print("The sum of %d and %d is: %d" % (num_1, num_2, summed))
print("The difference of %d and %d is: %d" % (num_1, num_2, difference))
print("The product of %d and %d is: %d" % (num_1, num_2, product))
try_divide()