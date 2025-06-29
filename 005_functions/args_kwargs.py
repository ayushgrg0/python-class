

"""
kwargs in functions
"""


def multiple_products(*args):  # funstion signature
    product = 1
    for items in args:
        product = product * items
    return product


print(multiple_products(2, 5, 4))


"""
Keywords using kwargs
"""


def name(**kwargs):
    first_name = kwargs.get("First_name")

    middle_name = kwargs["Middle_name"]

    last_name = kwargs["Last_name"]

    print(f"My first name is {first_name}.")
    print(f"My middle name is {middle_name}.")
    print(f"My last name is {last_name}.")


result = name(First_name="Ayush", Middle_name="Bahadur", Last_name="Gurung")
