# Before the conditionals, learn the comparison
#   < less than
#   > greater than
#   == is equal to
#   != not equal to

# Logicals
# and - both condition must be true to return true
# or - one of two or more condition must be true to return true
# not - just not

# Conditionals: if else
# var_bool = True
var_bool = False

if var_bool == True:
    print("Variable Bool: ", var_bool)
else:
    print("Variable Bool: ", var_bool)

if var_bool != True:
    print("False: ", var_bool)
else:
    print("True: ", var_bool)


# Example arithmetic
num1 = 12
num2 = 3
sum = num1 + num2 # 15
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
# modulus = 3 % 13
exponential = 5 ** 3
floordivision = 20 // 7 # answer 2

# uncomment to see the output
# print(sum)
# print(difference)
# print(product)
# print(quotient)
# print(modulus)
# print(exponential)
# print(exponential)
# print(exponential)
# print(floordivision)


# example of if elif else statements
x = 14

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")

        if x < 15:
            print("less than 15")
        elif x == 16:
            print("equal to 16")

    else:
        print("but not above 20.")
