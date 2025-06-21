
divisor = int(input("Enter a number : "))

dividend = 20

if divisor == 0:
    message = "Provide a valid number. The dividend cannot be divided by 0"
    raise Exception(message)

result = dividend / divisor
print("The result is ", result)


# 001_basics
# 002_datatypes
# 003_conditionals
# 004_loops
# 005_functions
# 006_classes
