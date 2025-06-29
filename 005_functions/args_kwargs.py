

'''
kwargs in functions
kwargs stands for keyword arguments. It allows you to pass a variable number of keyword arguments to a function.
This is useful when you want to pass a dictionary of key-value pairs to a function,
where the keys are the argument names and the values are the argument values.
'''


def multiple_products(*args):
    product = 1
    for items in args:
        product = product * items
    return product


print(multiple_products(2, 5, 4))
